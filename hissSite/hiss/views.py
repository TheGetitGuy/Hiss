import re
from django.shortcuts import render
from django.http import HttpResponse
from .models import userLoggedInData

#creating views

def login(request):
    
    return render(request, 'userLogin.html')
def register(request):
    
    return render(request, 'userRegister.html')

def userLoggedIn(request):
    context = {}
    if request.method == 'POST':
        
        context['userName'] = request.POST['userName']
        context['password'] = request.POST['password']
    return render(request,'userLoggedIn.html',context)