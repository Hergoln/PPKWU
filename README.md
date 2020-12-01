Third exercise of PPKWU course.

Applications starts by default as server connecting on address localhost with port 8000

To run application use command in PPKWU/exercise3 catalogue
```
python manage.py runserver
```

Application provides *calendar* endpoint.
*calendar* endpoint is a GET request that expects month as number as its argument
```
localhost:8000/calendar/<month>
```
or just empty *calendar* endpoint
```
localhost:8000calendar/
```

Exemplary links and their outputs:  
[http://localhost:8000/calendar/10]()
```
BEGIN:VCALENDAR

VERSION:2.0

PRODID:ics.py - http://git.io/lLljaA

BEGIN:VEVENT

DTSTART:20201010T120000Z

SUMMARY:Wielka Integracja WIP

UID:bf9ee7df-9699-48cd-99b0-337a7a631f31@bf9e.org

END:VEVENT

BEGIN:VEVENT

DTSTART:20201001T120000Z

SUMMARY:Akcja Integracja Online

UID:baec065f-c849-4117-a908-7ede45778d75@baec.org

END:VEVENT

BEGIN:VEVENT

DTSTART:20201009T120000Z

SUMMARY:Wielka Integracja WIP

UID:a30c832c-14f5-4475-ae19-f3909eca1504@a30c.org

END:VEVENT

BEGIN:VEVENT

DTSTART:20201008T120000Z

SUMMARY:Wielka Integracja WIP

UID:a532f48b-6335-414b-896d-c1ddcd29f9f0@a532.org

END:VEVENT

END:VCALENDAR

```

[http://localhost:8000/calendar/3]()
```
BEGIN:VCALENDAR

VERSION:2.0

PRODID:ics.py - http://git.io/lLljaA

BEGIN:VEVENT

DTSTART:20200317T120000Z

SUMMARY:Matura probna Matematyka rozszerzona

UID:633270b9-ca00-4992-a951-e7e30173fb44@6332.org

END:VEVENT

BEGIN:VEVENT

DTSTART:20200309T120000Z

SUMMARY:First Step to Fields Medal

UID:de2d95e3-8815-4d9a-b2be-ab309b090a98@de2d.org

END:VEVENT

BEGIN:VEVENT

DTSTART:20200313T120000Z

SUMMARY:FinaA konkursu InfoSukces

UID:6f02527e-c799-4521-80d9-7d54064c97ab@6f02.org

END:VEVENT

BEGIN:VEVENT

DTSTART:20200319T120000Z

SUMMARY:Matura probna Chemia rozszerzona

UID:36d3a112-577b-4f9a-94b3-58a7c5e0f77e@36d3.org

END:VEVENT

BEGIN:VEVENT

DTSTART:20200325T120000Z

SUMMARY:FinaA konkursu FascynujAca Fizyka - poziom ponadpodstawowy

UID:08fc312e-3477-4645-ba9f-e2b8a5a6a565@08fc.org

END:VEVENT

BEGIN:VEVENT

DTSTART:20200318T120000Z

SUMMARY:Matura probna Fizyka rozszerzona

UID:26ce0b9d-8c02-4857-aa55-4389ef408814@26ce.org

END:VEVENT

BEGIN:VEVENT

DTSTART:20200316T120000Z

SUMMARY:Matura probna Matematyka podstawowa

UID:b6779df2-572d-47a2-b070-31590e6d3779@b677.org

END:VEVENT

BEGIN:VEVENT

DTSTART:20200323T120000Z

SUMMARY:FinaA konkursu FascynujAca Fizyka - poziom podstawowy

UID:f833d308-41b0-49e2-8c4e-6937982a9627@f833.org

END:VEVENT

BEGIN:VEVENT

DTSTART:20200327T120000Z

SUMMARY:FinaA konkursu PiAkne doAwiadczenie\, FascynujAce WyjaAnienie

UID:e252f25c-88c2-4f92-ba0f-03cf0b198bec@e252.org

END:VEVENT

END:VCALENDAR

```

[March 2020 ics](https://hergoln.github.io/PPKWU//githubPagesRoot/example_march.ics)

[October 2020 ics](https://hergoln.github.io/PPKWU//githubPagesRoot/githubPagesRoot/example_october.ics)