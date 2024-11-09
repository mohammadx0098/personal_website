from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from .views import Home

urlpatterns = [
    path("", Home.as_view()),
]