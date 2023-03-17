from django.urls import path
from application1.views import something

app_name='something'
urlpatterns=[
    path('something/',something,name='something')
]