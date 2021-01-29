from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from tinymce.models import HTMLField
from django.core.validators import MaxValueValidator
# import datetime as dt


# Create your models here.
class Neighbourhood(models.Model):
    name=models.CharField(max_length=60)
    location=models.CharField(max_length=60)
    population=models.IntegerField()
    image = models.ImageField(upload_to = 'images/')

    def create_neigborhood(self):
        self.save()

    def delete_neigborhood(self):
        self.delete()

    @classmethod
    def search_by_name(cls,search_term):
        neighborhood=cls.objects.filter(name__icontains=search_term)
        return neighborhood


class Profile(models.Model):
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio=models.CharField(max_length=300)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

    def create_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Business(models.Model):
    name=models.CharField(max_length=60)
    description=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    email=models.EmailField()

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

class Post(models.Model):
    post=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
