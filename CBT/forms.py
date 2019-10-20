from django import forms
from django.contrib.auth.models import User
from .models import UserProfile,Therapist,CBT_therapy,WeeklySession,Challenge


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['username','email','password']


class UserProfileForm(forms.ModelForm):
    class Meta():
        model=UserProfile
        fields=['phone','age','region']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    
class TherapistForm(forms.ModelForm):
	class Meta():
		model=Therapist
		fields=['contact','region','name']


class CBT_therapyForm(forms.ModelForm):
	class Meta():
		model=CBT_therapy
		fields=['start_date','session_time','therapist','user']


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class RegisterCBTForm(forms.ModelForm):
	class Meta():
		model=CBT_therapy
		fields=['start_date','session_time']
		widgets = {
            'start_date': DateInput(),
            'session_time':TimeInput(),
        }



class WeeklySessionForm(forms.ModelForm):
	class Meta():
		model=WeeklySession
		fields=['session_date','session_time','challenge','week_no','therapy']
		

class ChallengeForm(forms.ModelForm):
	class Meta():
		model=Challenge
		fields=['title']