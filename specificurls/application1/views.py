from django.shortcuts import render
from django.http import HttpResponse


def something(request):
    return HttpResponse('yes this is the application 1 view')

