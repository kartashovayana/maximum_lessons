from django.shortcuts import render
from django.http import HttpResponse
def func(request):
    return HttpResponse("домашка по 4 занятию")

def index(request):
    return HttpResponse("12345")