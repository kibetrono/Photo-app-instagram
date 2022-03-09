from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib .auth import authenticate,login,logout# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from .forms import PictureUploadForm,CommentForm
from .models import Image,Profile,Likes,Comments
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .email import send_welcome_email


def index(request):
    images=Image.objects.all()
    context={'images':images}
    return render(request,'instagramapp/index.html',context)

def registerPage(request):
    form=UserCreationForm()
    if request.method == "POST":
        form_results=UserCreationForm(request.POST)
        if form_results.is_valid():
            user =form_results.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('index')

        else:
            messages.error(request, 'Error occured during registration')

    context = {'reg_form':form}
    return render(request, 'instagramapp/auth.html',context)

