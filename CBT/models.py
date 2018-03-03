from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from datetime import date
from django.utils import timezone
from datetime import datetime, timedelta


# Create your models here.

class Therapist(models.Model):
    name = models.CharField(max_length=20)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=17,blank=True) 
    region=models.CharField(max_length=30,default='online')
    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex],max_length=17,blank=True)
    age=models.IntegerField()
    region=models.CharField(max_length=30)
    def __unicode__(self):
        return self.user.username
    def get_region(self):
        return self.region

class CBT_therapy(models.Model):
    """docstring for CBT_therapy : has one to one relationship with user and therapist.
       Many to one relation with weekly session.
    """
    start_date = models.DateField()
    session_time=models.TimeField()
    therapist=models.ForeignKey(Therapist)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        unique_together = (('therapist', 'user'),)

class WeeklySession(models.Model):
    session_date=models.DateField()
    session_time=models.TimeField()
    week_no = models.IntegerField()
    challenge=models.CharField(max_length=150)
    therapy = models.ForeignKey(CBT_therapy)
    def is_past_due(self):
        return date.today() > self.session_date
    def start_session(self):
        if(date.today() == self.session_date):
            if(self.session <= timezone.now() and  timezone.now() < self.time.session_time + timedelta(hours=2)):
                return True

        
class Challenge(models.Model):
    title=models.CharField(max_length=150)
    def __unicode__(self):
        return self.title