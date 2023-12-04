from app1.views import *
from django.urls import path
app_name='river'
urlpatterns=[
    path('kaveri/',kaveri,name='kaveri'),
]