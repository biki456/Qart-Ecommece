from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=123)
    #avater = models.ImageField(upload_to="profile picture/")

