from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.contrib.auth.models import User, auth
from django.contrib import messages

def home(request):
    return render(request, 'index.html',)

def profile(request):
    return render(request, 'profile.html',)

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user= auth.authenticate(request, username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'error in login')
            return redirect('signin')
    else:
        return render(request, 'signin.html',)

def signup(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       first_name = request.POST['firstname']
       last_name = request.POST['lastname']
       email = request.POST['email']
       if User.objects.filter(username=username).exists():
        messages.info(request,'error')
        return redirect('signup')
       else:
        user= User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
        user.save()
        return redirect('signin')
    else:
        return render(request, 'signup.html',)




def logout(request):
    auth.logout(request)
    return redirect('signin')



def groups(request):
    return render(request, 'groups.html',)

def explore(request):
    return render(request, 'explore.html',)