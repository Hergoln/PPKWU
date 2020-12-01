from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from ics import Calendar, Event
import requests
import datetime
from bs4 import BeautifulSoup
import unicodedata

def calendar(request, month):
	year = datetime.datetime.now().year
	URL= "http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php"
	PARAMS = {'rok':year, 'miesiac':month, 'lang':1}
	r = requests.get(url=URL, params=PARAMS)
	soup = BeautifulSoup(r.text, 'html.parser')

	r = Calendar()
	for num, action in enumerate(soup.find_all("a", class_="active")):
		e = Event()

		e.name = unicodedata.normalize('NFD', soup.find_all("div", class_="InnerBox")[num].string).encode('ascii', 'ignore').decode("utf-8")
		print(str(year) + '-' + month + '-' + action.string + ' ' + '12:00')
		e.begin = str(year) + '-' + month + '-' + action.string + ' ' + '12:00'
		
		r.events.add(e)
	with open('../githubPagesRoot/example.ics', 'w') as exemplary_file:
	 	exemplary_file.writelines(r)

	return HttpResponse(r)
