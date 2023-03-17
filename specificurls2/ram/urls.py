from django.urls import path
from ram.views import ram
ram_name='ram'
urlpatterns=[
    path('ram/',ram,name='ram'),
]