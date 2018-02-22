from django import forms
from .models import UserProfile,Therapist,CBT_therapy,WeeklySession
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['username','email','password']

class UserProfileForm(forms.ModelForm):
    class Meta():
        model=UserProfile
        fields=['phone','age','region']

class TherapistForm(forms.ModelForm):
	class Meta():
		model=Therapist
		fields=['contact','region','name']

class CBT_therapyForm(forms.ModelForm):
	class Meta():
		model=CBT_therapy
		fields=['start_date','session_time','therapist','user']

class RegisterCBTForm(forms.ModelForm):
	class Meta():
		model=CBT_therapy
		fields=['start_date','session_time']

class WeeklySessionForm(forms.ModelForm):
	class Meta():
		model=WeeklySession
		fields=['session_date','session_time','challenge','week_no','therapy']
		