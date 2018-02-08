from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone=models.CharField(max_length=10)
    age=models.IntegerField()
    region=models.CharField(max_length=30)
