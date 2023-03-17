from django.shortcuts import render

# Create your views here.
def jinjatags(request):
    d={'a':210,'b':200,'c':30}
    return render(request,'jinjatags.html',d)