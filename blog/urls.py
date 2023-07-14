from django.contrib import admin
from django.urls import path

from blog import views 

#Url blogApp

urlpatterns = [
    path ('', views.blog1), 
    path ('blog2/',views.blog2), #para adcionar novas pags necesario usar /"caminho"
    path ('blog3/',views.blog3), #para adcionar novas pags necesario usar /"caminho"
]