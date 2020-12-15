Fourth exercise of PPKWU course.

Application starts by default as server connecting on addresss localhost with port 8000

To run application use command in PPKWU/exercise4 catalogue
```
python manage.py runserver
```

Application provides *vcard* endpoint.
*vcard* endpoint is a GET request that expects text used further by application to generate response filled with results from https://panoramafirm.pl/.
Every result has button that allows to create vCard for this particular result.

```
localhost:8000/vcard/<string>
```

