import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize

url ="http://vit.ac.in"

br = mechanize.Browser()

br.open(url)

for link in br.links():
	newurl = urlparse.urljoin(link.base_url,link.url)
	print newurl

