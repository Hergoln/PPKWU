Second exercise of PPKWU course.

Application starts by default as server connecting on address localhost with port 8000

To run application use command in PPKWU/exercise2 catalogue
```
python manage.py runserver
```

Application provides *string* endpoint.
*string* endpoint is a simple GET request that expects string as its sole argument and returns information about number of digits, special characters, lower and upper case letters as well as histogram of all characters occurring in given string accumulated to JSON format.

Exemplary links and their outputs:
[http://localhost:8000/string/Another%202020%20%20reference]()
```
{
   "lowerCase":15,
   "upperCase":1,
   "digits":4,
   "specialChar":3,
   "histogram":{
      "A":1,
      "n":2,
      "o":1,
      "t":1,
      "h":1,
      "e":5,
      "r":3,
      " ":3,
      "2":2,
      "0":2,
      "f":1,
      "c":1
   }
}
```
[http://localhost:8000/string/This%20is%20exemplary%20string%20with%2082%20lower%20case%20letters,%201%20upper%20case%20letters%206%20digits%20and%2019%20special%20characters]():
```
{
   "lowerCase":82,
   "upperCase":1,
   "digits":6,
   "specialChar":19,
   "histogram":{
      "T":1,
      "h":3,
      "i":7,
      "s":10,
      " ":18,
      "e":12,
      "x":1,
      "m":1,
      "p":4,
      "l":5,
      "a":7,
      "r":8,
      "y":1,
      "t":8,
      "n":2,
      "g":2,
      "w":2,
      "8":1,
      "2":1,
      "o":1,
      "c":5,
      ",":1,
      "1":2,
      "u":1,
      "6":1,
      "d":2,
      "9":1
   }
}
```
