from django.http import HttpResponse
from django.contrib.auth.models import User


def print_hello(request):
    if not request.user.is_authenticated:
        return HttpResponse(f"Go away or go to <a href='/admin/logout'>Logout</a>")

    return HttpResponse(f"Hello, {request.user} <a href='/admin/logout'>Logout</a>")
