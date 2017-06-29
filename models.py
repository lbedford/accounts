"""Models for accounts."""
from django.db import models
from django.contrib.auth.models import User

class LbwUser(models.Model):
  """A model to attach a photo to a user."""
  user = models.OneToOneField(User, primary_key=True,
                              on_delete=models.CASCADE)
  profile_image = models.ImageField(
      upload_to='img/',
      default='img/unknown.jpg')

  def __unicode__(self):
    return self.user.get_full_name()
