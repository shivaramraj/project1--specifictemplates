from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def nothing(request):
    
    return HttpResponse('this is the second application view')