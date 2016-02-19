import urllib
from bs4 import BeautifulSoup

url ="http://www.quora.com"
htmlfile = urllib.urlopen(url)
htmltext = htmlfile.read()

#print htmltext
soup = BeautifulSoup(htmltext,"lxml")
#print soup.prettify()
form_data = soup.findAll('form')
print form_data.findAll('text')