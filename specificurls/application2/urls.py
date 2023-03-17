from django.urls import path
from application2.views import nothing

app_name='nothing'

urlpatterns=[
    path('nothing/',nothing,name='nothing')
]