from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Create your models here.

class Therapist(models.Model):
    name = models.CharField(max_length=20,default='Not-Enrolled-yet')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=17,blank=True) 
    region=models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex],max_length=17,blank=True)
    age=models.IntegerField()
    region=models.CharField(max_length=30)
    therapist=models.OneToOneField(Therapist)
    def __unicode__(self):
        return self.user.username

class CBT_therapy(models.Model):
    """docstring for CBT_therapy : has one to one relationship with user and therapist.
       Many to one relation with weekly session.
    """
    start_date = models.DateField()
    therapist=models.OneToOneField(Therapist)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class WeeklySession(models.Model):
    session_date=models.DateField()
    session_time=models.TimeField()
    week_no = models.IntegerField()
    challenge=models.CharField(max_length=150)
    therapy = models.ForeignKey(CBT_therapy)

        