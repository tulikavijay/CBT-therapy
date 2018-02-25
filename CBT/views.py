from django.shortcuts import render
# for login and logout
from django.contrib.auth import login,authenticate,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Forms
from .forms import UserForm,UserProfileForm,CBT_therapyForm,RegisterCBTForm
#Models
from .models import Therapist,CBT_therapy
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
    if request.method == 'POST':
        register_form = RegisterCBTForm(request.POST or None)
        start_date=register_form.cleaned_data['start_date']
        session_time=register_form.cleaned_data['session_time']
        user=request.user
        username=UserProfileForm.objects.get(user=user)
        region=username.get_region()
        therapist=Therapist.objects.filter(region=region)
        cbt=CBT_therapy(
            user=user,
            start_date=start_date,
            session_time=session_time,
            therapist=therapist
            )
        cbt.save(force_insert=True)
    else:
        register_form = RegisterCBTForm()
    return render(request,'register_for_cbt.html',{'register_form':register_form})



def viewCBT(request):
    registered=False
    if request.user.is_authenticated():
        user=request.user
        if(CBT_therapy.objects.filter(user=user)):
            registered=True
        else:
            registered=False
    return render(request,'cbt.html',{registered:registered})