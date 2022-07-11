import re
from django.shortcuts import render
from django.http import HttpResponse

#creating views

def login(request):

    return render(request, 'userLogin.html')
def userLoggedIn(request):
    context = {}
    if request.method == 'POST':
        context['userName'] = request.POST['userName']
        context['password'] = request.POST['password']
    return render(request,'userLoggedIn.html',context)