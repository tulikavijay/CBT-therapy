
"""CBT_therapy URL Configuration"""

from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

from CBT import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('depression-test/',views.screen_test,name='screen_test'),
    path('register/',views.register,name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.signout, name='logout'),
    path('locate/',views.locate,name='locate'),
    path('CBT_therapy/',views.viewCBT,name='viewCBT'),
    path('register_for_therapy/',views.registerCBT,name='registerCBT'),
    path('dashboard/<int:id>/',views.dashboard,name='dashboard'),
    path('session/(\d+)/',views.session,name='session'),
    path('draw/(\d+)/',views.draw,name='draw'),
    path('sample-draw/<int:pk>/',views.sampleDraw,name='sampledraw'),    
]   
