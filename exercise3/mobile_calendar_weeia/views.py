from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from ics import Calendar, Event


def calendar(request, dateString, timeString, eventTitle):
    c = Calendar()
    e = Event()
    e.name = eventTitle
    e.begin = dateString + ' ' + timeString
    c.events.add(e)
    with open('example.ics', 'w') as exemplary_file:
        exemplary_file.writelines(c)
    return HttpResponse(c)
