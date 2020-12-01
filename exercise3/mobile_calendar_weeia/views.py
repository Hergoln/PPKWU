from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from ics import Calendar, Event
import requests
import datetime
from bs4 import BeautifulSoup
import unicodedata

def calendar(request, month):
	stuff = make_stuff(month)

	return HttpResponse(stuff)

def calendar_no_month(request):
	month = datetime.datetime.now().month
	stuff = make_stuff(month)
	r = HttpResponse()
	r.writelines(stuff)
	return  r

def make_stuff(month):
	year = datetime.datetime.now().year
	URL= "http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php"
	month = add_0_prefix_if_ness(month)
	# else:
	# 	PARAMS = {'rok':year, 'miesiac':month, 'lang':1}
	PARAMS = {'rok':year, 'miesiac':month, 'lang':1}
	print(month)
	r = requests.get(url=URL, params=PARAMS)
	soup = BeautifulSoup(r.text, 'html.parser')

	stuff = Calendar()

	for num, action in enumerate(soup.find_all("a", class_="active")):
		e = Event()

		e.name = unicodedata.normalize('NFD', soup.find_all("div", class_="InnerBox")[num].string).encode('ascii', 'ignore').decode("utf-8")
		print(str(year) + '-' + month + '-' + add_0_prefix_if_ness(action.string) + ' ' + '12:00')
		e.begin = str(year) + '-' + month + '-' + add_0_prefix_if_ness(action.string) + ' ' + '12:00'
		
		stuff.events.add(e)

	with open('../githubPagesRoot/example.ics', 'w') as exemplary_file:
	 	exemplary_file.writelines(stuff)
	return stuff

def add_0_prefix_if_ness(s):
	if int(str(s)) < 10:
		return '0' + str(s)
	return s