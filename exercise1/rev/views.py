from django.shortcuts import render

# Create your views here.
def rev(request, string):
    return string[::-1]