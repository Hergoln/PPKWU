from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def rev(request, string):
    return HttpResponse(string[::-1])