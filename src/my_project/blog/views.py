from django.http import HttpResponse


def blog(request):
    return HttpResponse('It\'s blog!')
