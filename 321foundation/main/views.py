from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from django.contrib import messages


#from blog import templates

def home_view(request):
	return render(request,"home.html",{})



# Create your views here.
