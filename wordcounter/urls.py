from django.contrib import admin
from django.urls import path, path
from . import views

urlpatterns = [
    path('', views.home, name='home')
]
