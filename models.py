"""Models for accounts."""
from django.db import models
from django.contrib.auth.models import User

class LbwUser(models.Model):
  """A model to attach a photo to a user."""
  user = models.OneToOneField(User, primary_key=True)
  profile_image = models.ImageField(
      upload_to='img/',
      default='pic_folder/None/no-img.jpg')

  def __unicode__(self):
    return self.user.__unicode__() # pylint: disable=E1101
