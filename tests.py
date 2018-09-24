from django.db import IntegrityError
from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase


from .models import LbwUser

class LbwUserPropertyTests(TestCase):
    user = None

    def setUp(self):
        user = get_user_model()()
        user.save()
        first_name = "My"
        last_name = "Name"

    def test_cannot_create_lbwuser_without_user(self):
        lbwUser = LbwUser()
        self.assertRaises(IntegrityError, lbwUser.save)

    def test_can_create_user_without_profile_picture(self):
        pass
        #lbwUser = LbwUser(user)
        #self.assertIs(True, True)

    def test_can_create_user_with_profile_picture(self):
        pass
        #lbwUser = LbwUser(user, profile_image='/path/to/image')
        #lbwUser.save()
        #self.assertIs(True, True)

class LbwUserMethodTests(TestCase):

    def test_unicode(self):
        pass
        #self.assertIs(user.__unicode__(), "%s %s" % (first_name, last_name))
