"""Models for accounts."""
from django.conf import settings
from django.db import models

class LbwUser(models.Model):
  """A model to attach a photo to a user."""
  user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True,
                              on_delete=models.CASCADE)
  profile_image = models.ImageField(
      upload_to='img/',
      default='img/unknown.jpg')

  def __unicode__(self):
    return self.user.get_full_name()

  def __str__(self):
    return self.user.get_full_name()
