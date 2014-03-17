from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class LbwUser(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    profile_image = models.ImageField(upload_to = 'img/', default = 'pic_folder/None/no-img.jpg')
