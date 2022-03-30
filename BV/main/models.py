from django.conf import settings
from django.db import models

# Create your models here.

class userProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=300, null=True)
    user_phone = models.CharField(max_length=20, null=True)
    user_address = models.CharField(max_length=20, null=True)
    date = models.DateTimeField(auto_now_add=True)
    bio = models.CharField(max_length=300, null=True)
    user_image = models.ImageField(blank=True, null=True, upload_to='media', default='user.png')