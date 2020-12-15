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

    for num, element in enumerate(soup.find_all('a', class_="company-name")):
        print(element.text)

        # listElementSoup = BeautifulSoup(str(element.string), 'html.parser')
        # for el in enumerate(listElementSoup.find_all('a', class_="company-name")):
        #     print(el)


    # with open('../githubPagesRoot/example.ics', 'w') as exemplary_file:
    #  	exemplary_file.writelines(stuff)
    return r 