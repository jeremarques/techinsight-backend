from django.urls import path
from django.shortcuts import HttpResponse

def hello(request):
    return HttpResponse('hello')

urlpatterns = [
    path('', hello)
]