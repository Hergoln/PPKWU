from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from collections import Counter
def stringAPI(request, string):
    data = {
        'lowerCase': sum(1 for c in string if c.islower()),
        'upperCase': sum(1 for c in string if c.isupper()),
        'digits': sum(1 for c in string if c.isdigit()),
        'specialChar': sum(1 for c in string if not c.isalpha() and not c.isdigit()),
        'histogram': Counter(string)
    }
    return JsonResponse(data)