from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import inputfood
from .forms import inputfoodform
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import Http404

def index(req):
	return render(req, 'myweb/index.html')

def home(req):
    inputfoods = inputfood.objects.all()
    return render(req, 'myweb/home.html', {'inputfoods': inputfoods})
    
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(request,username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'myweb/register.html', {'form': form})

def indexforadmin(request):
    print("Before go to if ")
    if request.method == 'POST':

        img = request.POST.get("img")
        namefood1 = request.POST.get("namefood1")
        namefood2 = request.POST.get("namefood2")
        add = inputfood(img=img,namefood1=namefood1,namefood2=namefood2)
        add.save()
        return redirect('home')
    return render(request, 'myweb/indexforadmin.html')

def indexforadmins(req):
    inputfoods = inputfood.objects.all()
    ins = {
        'inputfoods' : inputfoods
        }
    return render(req, 'myweb/indexforadmin.html', ins)