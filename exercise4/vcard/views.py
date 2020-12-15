from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def vcard(request, string):
    return HttpResponse(string) 