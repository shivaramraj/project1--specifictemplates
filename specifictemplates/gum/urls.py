from gum.views import gum
from django.urls import path
gum_name='gum'
urlpatterns=[
    path('gum/',gum,name='gum')
]