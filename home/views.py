# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse        

def home1(request):
    return HttpResponse('resposta da def home1 que vem da home')