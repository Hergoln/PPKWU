from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
def stringAPI(request, string):
    data = {
        'lowerCase': sum(1 for c in string if c.islower()),
        'upperCase': sum(1 for c in string if c.isupper()),
        'digits': sum(1 for c in string if c.isdigit()),
        'specialChar': sum(1 for c in string if not c.isalpha())
    }
    return JsonResponse(data)