from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url = 'login')
def home(request):
    # home index
    return render (request,'home.html')


def base(request):
    # home index
    return render (request,'base.html')