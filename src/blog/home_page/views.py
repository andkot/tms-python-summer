from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def index(requests):
    # return HttpResponse(f'This is a home page! {say_hello("User")}')
    name = "USER"
    return render(requests, 'home_page/index.html', locals())
