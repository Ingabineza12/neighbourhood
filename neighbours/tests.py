from django.test import TestCase
from . models import *

class ProfileTestClass(TestCase):

    def setUp(self):

        self.new_profile=Profile(bio='i love basketball')
    # test for instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))
    # testing the save mothod
    def test_save_profile(self):
        self.new_profile.create_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)>0)

class NeighbourhoodTestClass(TestCase):

        def setUp(self):
            self.new_neighbourhood=Neighbourhood(name='killeleshwa',population=20101000)
        def tearDown(self):
            Neighbourhood.objects.all().delete()


        # test for instance
        def test_instance(self):
            self.assertTrue(isinstance(self.new_neighbourhood,Neighbourhood))
        # test for save method
        def test_save_neighbourhood(self):
            self.new_neighbourhood.create_neigborhood()
            neighborhood=Neighbourhood.objects.all()
            self.assertTrue(len(neighborhood)>0)
        def test_delete_neighbourhood(self):
            self.new_neighbourhood.create_neigborhood()
            self.new_neighbourhood.delete_neigborhood()
            neighborhood=Neighbourhood.objects.all()
            self.assertEqual(len(neighborhood),0)
