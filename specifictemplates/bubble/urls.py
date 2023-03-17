from django.urls import path
from bubble.views import bubble
bubble_name='bubble'
urlpatterns=[
    path('bubble/',bubble,name='bubble')
]