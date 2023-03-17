from django.shortcuts import render

# Create your views here.
def gum(request):
    return render(request,'sample.html')
