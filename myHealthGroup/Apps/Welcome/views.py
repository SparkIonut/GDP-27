from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import User_Login

def Welcome(request):
    return render(request, 'Welcome/Welcome.html')

def Ethics(request):
    return render(request, 'Welcome/Ethics.html')

def Terms(request):
    return render(request, 'Welcome/Terms.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('blog:blog')
        else:
            form = User_Login()
            return render(request, 'Welcome/Login.html',{'form':form})
    else:
        form = User_Login()
        return render(request, 'Welcome/Login.html',{'form':form})