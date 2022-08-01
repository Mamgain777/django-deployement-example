from wsgiref.util import request_uri
from django.shortcuts import render
from basic_app.forms import UserProfileInfoForm,UserForm
from basic_app.models import User,UserProfileInfo

# Setting for user login
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



# Create your views here.

def index(request):

    return render(request,'basic_app/index.html',{'name':'Home'})


def special(request):
    return render(request,'basic_app/special.html',{'name':"Special"})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(index))

def form(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if profile_form.is_valid() and user_form.is_valid():
            print('reached 1')
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                print('Found It!')
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
            print(f'username: {user.username}\npassword:{user.password}')
        else:
            print(user_form.errors,profile_form.errors)

    
    profile_form = UserProfileInfoForm()
    user_form = UserForm()
    return render(request,'basic_app/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered,'name':'register'})


def user_login(request):

    if request.method == "POST":
        # print('Check Point 1')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticating Login 
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                # print('Check Point A')
                return HttpResponseRedirect(reverse(special))
            else:
                return HttpResponse("Account not active")

        else:
            print('***Someone tried to login using followinf information***')
            print(f'Username: {username}\nPassword: {password}')
            return HttpResponse('Invalid Login Details')
    
    else:
        return render(request,'basic_app/login.html',{})

        