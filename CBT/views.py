from django.shortcuts import render
# for login and logout
from django.contrib.auth import login, authenticate,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Forms
from .forms import UserForm,UserProfileForm,CBT_therapyForm
#Models
from .models import Therapist
# Create your views here.
def index(request):
    return render(request,'home.html',{})

def screen_test(request):
    return render(request,'screen_test.html',{})

def register(request):

    registered=False
    if request.method =='POST':
        user_form=UserForm(request.POST or None)
        profile_form=UserProfileForm(request.POST or None,request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user_form.cleaned_data.get('password'))
            username=user_form.cleaned_data.get('username')
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
           # Update our variable to tell the template registration was successful.
            registered=True
            login(request,user)
    else:
        user_form=UserForm()
        profile_form=UserProfileForm()

    return render(request,'register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def locate(request):
    return render(request,'map.html',{})

def registerCBT(request):
    registered=False
    if request.method == 'POST':
        cbt_therapy_form=CBT_therapyForm(request.POST or None)

        if cbt_therapy_form.is_valid():
            cbt_form=cbt_therapy_form.save()
            region=cbt_therapy_form.cleaned_data.get('region')
            cbt_form.therapist=Therapist.objects.filter(region=region)
            cbt_form.save()
            registered=True
    else:
        cbt_therapy_form=CBT_therapyForm()
    return render(request,'register_for_cbt.html',{'cbt_therapy_form':cbt_therapy_form,'registered':registered})

