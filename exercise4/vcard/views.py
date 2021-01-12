from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse


def vcard(request, string):
    return HttpResponse(make_stuff(string))

def result(request, string):
    return HttpResponse(createVCard(string))

def make_stuff(searchQuery):
    URL= "https://panoramafirm.pl/szukaj?k=" + '+'.join(searchQuery.split()) + "&l="
    r = requests.get(url=URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    numberOfCompaniesOnFirstPage = len(soup.find_all('a', class_="company-name"))

    # w endStrings leżą sobie pod koniec tej funkcji prawie całe vCardy, trzeba by je 
    # jeszcze przerobić na odpowiedni format
    endStrings = ['' for i in range(numberOfCompaniesOnFirstPage)]
    titles = ['' for i in range(numberOfCompaniesOnFirstPage)]
    hrefs = ['' for i in range(numberOfCompaniesOnFirstPage)]
    for num, el in enumerate(soup.find_all('li', class_='company-item')):
        for item, element in enumerate(el.find_all('a', class_="company-name")):
            if element is not None:
                endStrings[num] += element.text.strip()
                hrefs[num] += element['href']
                titles[num] += element.text.strip()
            endStrings[num] += ']['

        for _, element in enumerate(el.find_all('div', class_="address")):
            if element is not None:
                endStrings[num] += element.text.strip()
            endStrings[num] += ']['

        for _, element in enumerate(el.find_all('a', class_="icon-telephone")):
            if element is not None:
                endStrings[num] += element.get('title').strip()
            endStrings[num] += ']['

        for _, element in enumerate(el.find_all('a', class_="icon-website")):
            href = element.get('href')
            if href is not None:
                endStrings[num] += href.strip()
            endStrings[num] += ']['

            
        for _, element in enumerate(el.find_all('a', class_="icon-envelope")):
            title = element.get('title')
            if title is not None:
                endStrings[num] += title.strip()
            endStrings[num] += ']['

    htmlString = ''
    for index in range(len(endStrings)):
        endStrings[index] = endStrings[index].replace('https://', '')
        endStrings[index] = endStrings[index].replace('http://', '')
        htmlString += titles[index] + ' : <a href="http://localhost:8000/vcard/result/' + endStrings[index] + '">GENERUJ VCARD</a></br>'
    return htmlString


def createVCard(data):
    hymySring = ''
    hymySring += data
    for i in data.split(']['):
        hymySring += i + "</b>"
    vcardInString = ''

    vcardInString += 'BEGIN:VCARD'
    vcardInString += 'VERSION:4.0'
    # here is code for generation



    vcardInString += 'END:VCARD'
    return hymySring