import urllib
from bs4 import BeautifulSoup

htmlfile = urllib.urlopen("http://www.reddit.com")
#htmltext = htmlfile.read()

soup = BeautifulSoup(htmlfile,"lxml")
reddit_tags = soup.find_all('a')
for tag in reddit_tags:
	print tag.get('href')
