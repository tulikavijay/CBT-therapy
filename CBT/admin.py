from django.contrib import admin
from .forms import UserForm,UserProfileForm
from .models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display=["__unicode__","phone","age","region"]
    form=UserProfileForm
