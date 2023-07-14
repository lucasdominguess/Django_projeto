from django.contrib import admin
from django.urls import path

from blog import views 

#Url blogApp

urlpatterns = [
    path ('', views.blog1), 
]