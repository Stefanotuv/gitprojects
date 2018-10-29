"""
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from exercise import views

urlpatterns = [
    path('', views.exercise, name="exercise"),
    path('users', views.users, name="users"),
    path('', views.index, name="index"),

]
