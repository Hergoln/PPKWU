from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def vcard(request, string):
    return HttpResponse(make_stuff(string))

def make_stuff(searchQuery):
    URL= "https://panoramafirm.pl/szukaj?k=" + '+'.join(searchQuery.split()) + "&l="
    print(URL)
    # r = requests.get(url=URL)
    # soup = BeautifulSoup(r.text, 'html.parser')


    # for num, action in enumerate(soup.find_all("a", class_="active")):
    # 	e = Event()

    # 	e.name = unicodedata.normalize('NFD', soup.find_all("div", class_="InnerBox")[num].string).encode('ascii', 'ignore').decode("utf-8")
    # 	print(str(year) + '-' + month + '-' + add_0_prefix_if_ness(action.string) + ' ' + '12:00')
    # 	e.begin = str(year) + '-' + month + '-' + add_0_prefix_if_ness(action.string) + ' ' + '12:00'

    # 	stuff.events.add(e)

    # with open('../githubPagesRoot/example.ics', 'w') as exemplary_file:
    #  	exemplary_file.writelines(stuff)
    return URL 