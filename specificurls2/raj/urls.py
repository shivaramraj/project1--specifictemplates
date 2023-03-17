from raj.views import raj,raj2
from django.urls import path
ram_name='raj'
urlpatterns=[
    path('raj/',raj,name='raj'),
    path('raj2/',raj2,name='raj2'),
]