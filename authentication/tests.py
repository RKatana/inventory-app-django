from django.contrib.auth import get_user_model
from django.db.models.expressions import Value
from django.test import TestCase

# Create your tests here.
<<<<<<< HEAD
class TestProfile(TestCase):
  def setUp(self):
    self.new_user = User(username = "muturi")
    self.new_user.save()
    self.newprofile = Profile.objects.create(profilePic='', bio='engineer')

  def tearDown(self):
    Profile.objects.all().delete()
    User.objects.all().delete()

  def test_isinstance(self):
    self.assertTrue(isinstance(self.newprofile, Profile))
=======
class UserManagerTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='carpenter@user.com', password='foo')
        self.assertEqual(user.email, 'carpenter@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="foo")


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
>>>>>>> 9e956906a8ff7509db94fa0172500e00ca1ab070
