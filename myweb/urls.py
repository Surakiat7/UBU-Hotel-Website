from django.urls import path
from django.contrib.auth import views as aunt_views

from . import views
from django.contrib.auth import views as auth_views
from . import *

urlpatterns = [
    path('', views.index, name='index'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('login',auth_views.LoginView.as_view(template_name='myweb/login.html'),name='login'),
    path('register', views.signup, name='register'),
    path('indexforadmin', views.indexforadmin, name='indexforadmin'),
    path('home', views.home, name='home'),
]