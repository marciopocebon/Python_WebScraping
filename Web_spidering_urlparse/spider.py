import urlparse
import urllib
from bs4 import BeautifulSoup

url = "http://nytimes.com"

urls = [url] #stack of urls still to scrape
visited = [url] #visited record of urls

while len(urls) > 0 :
	try:
		htmltext = urllib.urlopen(urls[0]).read()
	except:
		print urls[0]
	soup = BeautifulSoup(htmltext,"lxml")
		
	urls.pop(0)
	
	#print soup.findAll('a',href=True)
	for tag in soup.findAll('a',href=True):
		print tag['href']
