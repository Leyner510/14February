from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('photo', views.photo, name='photo'),
    path('words', views.words, name='words'),


]