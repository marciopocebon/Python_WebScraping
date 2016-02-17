import urllib2
from bs4 import BeautifulSoup

url = "http://www.imdb.com/search/title?sort=num_votes,desc&start=1&title_type=feature&year=2005,2016"

htmlfile = urllib2.urlopen(url)
htmltext = htmlfile.read()
htmlfile.close()

soup = BeautifulSoup(htmltext,"lxml")
for movie in soup.findAll('td','title'):
	title = movie.find('a').contents[0]
	genres = movie.find('span','genre').findAll('a')
	#for g in genres:
	#	genres.append( g.contents[0])
	genres = [g.contents[0] for g in genres]
	runtime = movie.find('span','runtime').contents[0]
	rating = movie.find('span','value').contents[0]
	print title,genres,runtime,rating