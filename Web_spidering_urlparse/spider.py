import urlparse
import urllib
from bs4 import BeautifulSoup

url = "http://vit.ac.in"

urls = [url] #stack of urls still to scrape
visited = [url] #visited record of urls

while len(urls) >0:
	try:
		htmltext = urllib.urlopen(urls[0]).read()
	except:
		print urls[0]
	soup = BeautifulSoup(htmltext,"lxml")
		
	urls.pop(0)
	print len(urls)

	#print soup.findAll('a',href=True)
	for tag in soup.findAll('a',href=True):
		tag['href'] = urlparse.urljoin(url,tag['href'])
		if url in tag['href'] and tag['href'] not in visited:
			urls.append(tag['href'])
			visited.append(tag['href'])
print visited
