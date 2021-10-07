from django.test import TestCase

# Create your tests here.
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
