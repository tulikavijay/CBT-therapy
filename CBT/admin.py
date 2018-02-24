from django.contrib import admin
from .forms import UserForm,UserProfileForm,TherapistForm,CBT_therapyForm,WeeklySessionForm
from .models import UserProfile,Therapist,CBT_therapy,WeeklySession

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display=["__unicode__","phone","age","region"]
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

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Therapist,TherapistAdmin)
admin.site.register(CBT_therapy,CBT_therapyAdmin)
admin.site.register(WeeklySession,WeeklySessionAdmin)



