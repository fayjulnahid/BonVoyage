from django.shortcuts import render
from django.http import HttpResponse


def hi(request):
    return HttpResponse('<h1>This page works</h1>')
