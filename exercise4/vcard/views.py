from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse


def vcard(request, string):
    return HttpResponse(make_stuff(string))

def make_stuff(searchQuery):
    URL= "https://panoramafirm.pl/szukaj?k=" + '+'.join(searchQuery.split()) + "&l="
    print(URL)
    r = requests.get(url=URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    numberOfCompaniesOnFirstPage = len(soup.find_all('a', class_="company-name"))

    endStrings = ['' for i in range(numberOfCompaniesOnFirstPage)]

    for num, element in enumerate(soup.find_all('a', class_="company-name")):
        endStrings[num] += element.text + '::'

    for num, element in enumerate(soup.find_all('div', class_="address")):
        endStrings[num] += element.text + '::'

    for num, element in enumerate(soup.find_all('a', class_="icon-telephone")):
        print(element.text)

    return r 