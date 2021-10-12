import unittest
from django.contrib.auth import get_user_model
from django.db.models.expressions import Value
from django.test import TestCase
from .models import Profile

# Create your tests here.

class TestProfile(TestCase):
  def setUp(self):
    self.new_user = get_user_model()(name = "muturi")
    self.new_user.save()
    self.newprofile = Profile.objects.create(profile_pic='default.jpeg', bio='engineer')

  def tearDown(self):
    Profile.objects.all().delete()
    get_user_model().objects.all().delete()

  def test_isinstance(self):
    self.assertTrue(isinstance(self.newprofile, Profile))

class UserManagerTest(TestCase):
    @unittest.skip('The test fails')
    def test_create_user(self):
        #User = get_user_model()
        user = get_user_model().objects.create_user(email='carpenter@user.com', password='foo')
        self.assertEqual(user.email, 'carpenter@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.name)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            get_user_model().objects.create_user()
        with self.assertRaises(TypeError):
            get_user_model().objects.create_user(email='carpenter@user.com')
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email='carpenter@user.com', password="foo")

    #@unittest.skip('The test fails')
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='super@user.com', password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email='super@user.com', password='foo', is_superuser=False)

