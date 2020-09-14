from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render


def print_hello(request):
    if not request.user.is_authenticated:
        return HttpResponse(f"Go away or go to <a href='/admin/logout'>Logout</a>")

    return HttpResponse(f"Hello, {request.user} <a href='/admin/logout'>Logout</a>")

def home(request):
    users = User.objects.all()
    return render(request, 'index.html', context={'users': users})

def get_users(request):
    return home(request)

def get_user(request, username):
    user = User.objects.get(username=username)
    return render(request, 'user.html', context={'user': user})

