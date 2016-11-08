from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def Account(request, account_id):
    Account = get_object_or_404(User, pk = account_id)
    return render(request, 'Account/Account.html', {'Account' : Account})

def My_Account(request):
    return render(request, 'Account/My_Account.html')

def Logout(request):
    del request.session
    return redirect('welcome:welcome')
