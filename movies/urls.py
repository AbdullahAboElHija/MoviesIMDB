from django.urls import path
from . import views
from django.shortcuts import render

app_name = 'movies'

urlpatterns = [
    path('', views.movies_list, name='list'),
    path('create/', views.movie_create, name='create'),
    path('<slug:slug>/', views.movie_detail, name='detail'),
]
