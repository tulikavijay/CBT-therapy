
"""CBT_therapy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from CBT import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name='home'),
    url(r'^depression-test/',views.screen_test,name='screen_test'),
    url(r'^register/',views.register,name='register'),
    url(r'^login/$', auth_views.login,{'template_name': 'login.html'}, name='login'),
    url(r'^logout/',auth_views.logout,name='logout'),
    url(r'^locate/',views.locate,name='locate'),
    url(r'^CBT_therapy/',views.viewCBT,name='viewCBT'),
    url(r'^Register_for_therapy/',views.registerCBT,name='registerCBT'),
    url(r'^dashboard/',views.dashboard,name='dashboard'),
    url(r'^session/(\d+)/',views.session,name='session'),
    url(r'^draw/(\d+)/',views.draw,name='draw'),
]   
