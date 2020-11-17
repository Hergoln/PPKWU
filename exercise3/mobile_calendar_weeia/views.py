from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def calendar(request, dateString, timeString, eventTitle):
    return HttpResponse(dateString + " " + timeString + ":\n" + eventTitle)