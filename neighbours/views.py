from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .forms import *

# Create your views here.

def home(request):
    neighbourhoods = Neighbourhood.objects.all()
    return render(request, 'home.html',{"neighbourhoods":neighbourhoods,})


@login_required(login_url='/accounts/login/')
def neighbourhood(request):
    neighbourhoods = Neighbourhood.objects.all()
    return render(request,'home.html',{"neighbourhoods":neighbourhoods})


@login_required(login_url='/accounts/login/')
def myprofile(request,username=None):
    current_user=request.user
    profile=Profile.objects.filter(user=current_user)
    if not username:
        username=request.user.username
        images=Profile.objects.filter(bio=username)
    return render(request,'myprofile.html',locals(),{"profile":profile})

@login_required(login_url='/accounts/login/')
def profile_edit(request):
    current_user=request.user
    if request.method=='POST':
        form=UpdatebioForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.user=current_user
            image.save()
        return redirect('home')
    else:
        form=UpdatebioForm()
    return render(request,'registration/profile_edit.html',{"form":form})


@login_required(login_url='/accounts/login/')
def addneighbourhood(request):
    neighbourform = NeighbourhoodForm()
    neighbourform.owner = request.user
    if request.method == "POST":
        neighbourform = NeighbourhoodForm(request.POST,request.FILES)
        if neighbourform.is_valid():
           neighbourform.save()
           return render (request,'home.html')
        else:
           neighbourform=NeighbourhoodForm(request.POST,request.FILES)

    return render(request,'neighbourhood_form.html',{"neighbourform":neighbourform})


def neighbourhood_details(request,neighbourhood_id):
    businesses=Business.objects.filter(neighborhood=neighbourhood_id)
    posts=Post.objects.filter(neighborhood=neighbourhood_id)
    neighbourhood=Neighbourhood.objects.get(pk=neighbourhood_id)
    return render(request,'details.html',{'neighbourhood':neighbourhood,'businesses':businesses,'posts':posts})


@login_required(login_url="/accounts/login/")
def new_business(request,pk):
    current_user = request.user
    neighborhood = get_object_or_404(Neighbourhood,pk=pk)
    if request.method == 'POST':
        business_form = NewBusinessForm(request.POST, request.FILES)
        if business_form.is_valid():
            business = business_form.save(commit=False)
            business.user = current_user
            business.neighborhood=neighborhood
            business.save()
        return redirect('detail', neighbourhood_id=neighborhood.id)

    else:
        business_form = NewBusinessForm()
    return render(request, 'new_business_form.html', {"form": business_form,'neighborhood':neighborhood})

@login_required(login_url="/accounts/login/")
def new_post(request,pk):
    current_user = request.user
    neighborhood = get_object_or_404(Neighbourhood,pk=pk)
    if request.method == 'POST':
        post_form = NewPostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = current_user
            post.neighborhood=neighborhood
            post.save()
        return redirect('detail', neighbourhood_id=neighborhood.id)

    else:
        post_form = NewPostForm()
    return render(request, 'new_post_form.html', {"form": post_form,'neighborhood':neighborhood})


def search_hoods(request):
    if 'search' in request.GET and request.GET['search']:
        search_term=request.GET.get('search')
        searched_hoods=Neighbourhood.search_by_name(search_term)
        message=f'{search_term}'

        return render(request,'search.html',{"message":message,"searched_hoods":searched_hoods})

    else:
        message='You Havent searched for any term'

        return render(request, 'search.html',{"message":message})
