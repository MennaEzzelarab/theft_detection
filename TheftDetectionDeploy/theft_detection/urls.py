from django import views
from django.urls import path, include
from api import views

urlpatterns = [
    path('', include('api.urls')),
]