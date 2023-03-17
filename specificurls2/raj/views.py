from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def raj(request):
    return HttpResponse('this is the viw of raj')
def raj2(request):
    return HttpResponse('this is the second view of raj')