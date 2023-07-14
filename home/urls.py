from django.contrib import admin
from django.urls import path
from home import views 


#Url homeApp ok

urlpatterns = [
    path ('', views.home1), #link do app . chamando def home1 da views do app homeApp

]