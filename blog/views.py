# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse        

def blog1(request):
    return HttpResponse('resposta da def blog1 que vem da app "blog"')