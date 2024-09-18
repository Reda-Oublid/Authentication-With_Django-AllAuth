from django.contrib.auth.models import User, Group
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, max_length=155)
    avatar = models.ImageField(upload_to='Profile_Images', default='default_profile.JPG')
    preferences = models.CharField(choices=[('work', 'work'), ('Gamer', 'Gamer'), ('miner', 'miner')], max_length=15)
    birthdate = models.DateField(null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    country = models.CharField(null=True, blank=True, max_length=16)

    def __str__(self):
        return self.user.username
