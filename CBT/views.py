from django.shortcuts import render,redirect
# for login and logout
from django.contrib.auth import login,authenticate,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Forms
from .forms import UserForm,UserProfileForm,CBT_therapyForm,RegisterCBTForm
#Models
from .models import Therapist,CBT_therapy,User,UserProfile,Challenge,WeeklySession
from datetime import datetime, timedelta

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
        if register_form.is_valid():
            start_date=register_form.cleaned_data['start_date']
            session_time=register_form.cleaned_data['session_time']
            user=request.user
            username=UserProfile.objects.get(user=user)
            region=username.get_region()
            try:
                therapist_name=Therapist.objects.get(region=region)
            except : 
                therapist_name=Therapist.objects.get(region='online')
            cbt=CBT_therapy(
                user=user,
                start_date=start_date,
                session_time=session_time,
                therapist=therapist_name
                )
            cbt.save()
            session_date=start_date
            for challenge in Challenge.objects.all():
                session_date = session_date + timedelta(days=7)
                w=WeeklySession(
                     session_time =session_time,
                     session_date =session_date,
                     week_no=challenge.pk,
                     challenge=challenge.title,
                     therapy=cbt
                    )
                w.save()
    else:
        register_form = RegisterCBTForm()
    return render(request,'register_for_cbt.html',{'register_form':register_form})



def viewCBT(request):
    registered=False
    if request.user.is_authenticated():
        user=request.user
        try:
            temp=CBT_therapy.objects.filter(user=user)
            registered=True
            print(registered)
        except:
            registered=False
    return render(request,'cbt.html',{registered:registered})

@login_required
def dashboard(request):
    user=request.user
    username=UserProfile.objects.get(user=user)
    try:
        cbt=CBT_therapy.objects.get(user=user)
        therapy=WeeklySession.objects.select_related().filter(therapy=cbt)
    except:
        therapy=False
    return render(request,'dashboard.html',{'user':username,'therapy':therapy,'cbt':cbt})

@login_required
def session(request,pk):
    user=request.user
    username=UserProfile.objects.get(user=user)
    cbt=CBT_therapy.objects.get(user=user)
    therapy=WeeklySession.objects.select_related().get(pk=pk)
    attended=WeeklySession.objects.select_related().filter(therapy=cbt)
    session_active=therapy.start_session()
    # therapist=Therapist.objects.get(name=cbt.therapist)
    return render(request,'session.html',{'session_active':session_active,'therapy':therapy,'cbt':cbt,'attended':attended})

@login_required
def draw(request,pk):
    week=WeeklySession.objects.get(pk=pk)
    challenge=week.challenge
    return render(request,'draw.html',{'challenge':challenge})

def sampleDraw(request,pk):
    challenge=Challenge.objects.get(pk=pk)
    return render(request,'draw.html',{'challenge':challenge.title})