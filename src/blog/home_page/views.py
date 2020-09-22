from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(requests):
    return HttpResponse(f'This is a home page! {say_hello("User")}')
