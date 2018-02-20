from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Therapist(models.Model):
	# DEFAULT_THERAPIST = ''
	name = models.CharField(max_length=20,default='Not-Enrolled-yet',editable=False)
	contact=models.IntegerField()
	region=models.CharField(max_length=30)
	def __unicode__(self):
		return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone=models.CharField(max_length=10)
    age=models.IntegerField()
    region=models.CharField(max_length=30)
    therapist=models.ForeignKey(Therapist)
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

		