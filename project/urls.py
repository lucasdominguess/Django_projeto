"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include

#Url principal (raiz do projeto ) 

#Digitar aqui o caminho da pagina (usuario devera digitar o mesmo caminho para acessar a pag)

urlpatterns = [        #anhinando urls com include.
    path('admin/', admin.site.urls), 
    path ('home/', include ('home.urls')), #puxando a urls de homeApp
    path('blog/', include ('blog.urls')), #nao necessario colocar a barra
   # path ('blog2',include ('blog.urls')), #nao é necessario colocar segunda pagina se a primeiro caminho ja estiver incluso
    
]