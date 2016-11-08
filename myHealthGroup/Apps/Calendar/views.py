from django.shortcuts import render

def Calendar(request):
    return render(request, 'Calendar/Calendar.html')