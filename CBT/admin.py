from django.contrib import admin
from .forms import UserForm,UserProfileForm,TherapistForm,CBT_therapyForm,WeeklySessionForm,ChallengeForm
from .models import UserProfile,Therapist,CBT_therapy,WeeklySession,Challenge

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display=["__str__","phone","age","region"]
    form=UserProfileForm

class TherapistAdmin(admin.ModelAdmin):
	list_display=['name','contact','region']
	form=TherapistForm

class CBT_therapyAdmin(admin.ModelAdmin):
	list_display=['start_date','therapist','user']
	form=CBT_therapyForm

class WeeklySessionAdmin(admin.ModelAdmin):
	list_display=['session_date','session_time','week_no','challenge','therapy']
	form=WeeklySessionForm

class ChallengeAdmin(admin.ModelAdmin):
	list_display=['title']
	form=ChallengeForm

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Therapist,TherapistAdmin)
admin.site.register(CBT_therapy,CBT_therapyAdmin)
admin.site.register(WeeklySession,WeeklySessionAdmin)
admin.site.register(Challenge,ChallengeAdmin)




