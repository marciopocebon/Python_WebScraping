import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize

url ="http://cnn.com"
base = 'http://cnn.com'
htmlfile = urllib.urlopen(url)

soup = BeautifulSoup(htmlfile,"lxml")
#print htmlfile
for tag in soup.findAll('a',href=True):
	print base+"/"+ tag['href']
