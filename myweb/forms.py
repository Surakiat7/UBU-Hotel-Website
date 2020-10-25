from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import inputfood
from django.forms import ModelForm

class inputfoodform(ModelForm):
    class Meta:
        model = inputfood
        fields = ['img','namefood1','namefood2']