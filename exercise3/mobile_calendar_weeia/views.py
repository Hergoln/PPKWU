from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def calendar(request, string):
    return HttpResponse(string)