import urllib2
from bs4 import BeautifulSoup




jm = 'https://en.wikipedia.org/wiki/Jos%C3%A9_Mourinho'

page = urllib2.urlopen(jm)
soup = BeautifulSoup(page, "html.parser")
x = soup.body.find("table", attrs ={"class": "wikitable"})

print x