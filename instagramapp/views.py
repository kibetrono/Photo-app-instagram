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


def loginPage(request):
    page='login'
    if request.user.is_authenticated:
        return  redirect('index')

    if request.method == "POST":
        username=request.POST.get('username').lower()
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request, 'Username OR Password does not exist')

    context={'page':page}
    return render(request, 'instagramapp/auth.html', context)


def logoutUser(request):
    logout(request)
    return redirect('index')

@login_required(login_url='login')
def uploadPicture(request):

    form = PictureUploadForm()
    if request.method == "POST":
        form_results = PictureUploadForm(request.POST,request.FILES)
        if form_results.is_valid():

            form_results.save()
            return redirect('index')

    context = {"form": form}
    return render(request, 'instagramapp/upload_picture.html', context)


@login_required(login_url='login')
def my_images(request):
    current_user = request.user
    images = Profile.objects.filter(user_id=current_user.id).first()
    profiles = Image.objects.filter(user_id=current_user.id)

    return render(request, 'instagramapp/profile.html', {"profile": images,"images":profiles})

@login_required(login_url='login')
def each_image(request, id):
    image = Image.objects.get(id=id)
    return render(request, 'instagramapp/image_details.html', {'image': image})


@login_required(login_url='login')
def like_picture(request, id):
    likes = Likes.objects.filter(image_id=id).first()
    if Likes.objects.filter(image_id=id, user_id=request.user.id).exists():
        likes.delete()
        image = Image.objects.get(id=id)
        if image.likes_number == 0:
            image.likes_number = 0
            image.save()
        else:
            image.likes_number -= 1
            image.save()
        return redirect('/')
    else:
        likes = Likes(image_id=id, user_id=request.user.id)
        likes.save()
        image = Image.objects.get(id=id)
        image.likes_number = image.likes_number + 1
        image.save()
        return redirect('/')

@login_required(login_url='login')
def comment(request,pk):
    profile = Image.objects.get(pk=pk)
    form_results = CommentForm(request.POST,instance=profile)
    if request.method == "POST":
        if form_results.is_valid():
            user = request.user
            comment= form_results.cleaned_data['comment']
            comment_content = Comments(user=user, image=profile, comment=comment, created_on=datetime.now())
            comment_content.save()
            profile.comments_number = profile.comments_number + 1
            profile.save()

            return redirect('index')
        else:
            print('form is invalid')
    else:
        form_results = CommentForm

    context = {'form':form_results,'image':profile}
    return render(request,'instagramapp/comments.html',context)
