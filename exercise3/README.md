Third exercise of PPKWU course.

Applications starts by default as server connecting on address localhost with port 8000

To run application use command in PPKWU/exercise3 catalogue
```
python manage.py runserver
```

Application provides *calendar* endpoint.
*calendar* endpoint is a GET request that expects three string values as elements of url path.
Endpoint uses path calendar/<date>/<time>/<event-title>
Values in *<>* brackets are parts of event created using *calendar* endpoint. As names suggest *date* is date of an event, *time* is time of an event and *event-title* is title of event.

Exemplary links and their outputs:  
[http://localhost:8000/calendar/2020-11-17/15:15/tytuł wydarzenia]()
```
BEGIN:VCALENDAR 
VERSION:2.0 
PRODID:ics.py - http://git.io/lLljaA 
BEGIN:VEVENT 
DTSTART:20201117T151500Z 
SUMMARY:tytuł wydarzenia 
UID:d2b4dbb6-99ff-4080-a8b3-79a3a88d0973@d2b4.org 
END:VEVENT 
END:VCALENDAR
```

[http://localhost:8000/calendar/1997-09-24/21:37/tutuł innego wydarzenia]()
```
 BEGIN:VCALENDAR
 VERSION:2.0
 PRODID:ics.py - http://git.io/lLljaA
 BEGIN:VEVENT
 DTSTART:19970924T213700Z
 SUMMARY:tutuł innego wydarzenia
 UID:19f09c50-d6b3-4aa4-84f1-1132deeb7d67@19f0.org
 END:VEVENT END:VCALENDAR
```