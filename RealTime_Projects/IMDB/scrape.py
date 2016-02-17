import urllib2
from bs4 import BeautifulSoup

url = "http://www.imdb.com/search/title?sort=num_votes,desc&start=1&title_type=feature&year=2005,2016"

htmlfile = urllib2.urlopen(url)
htmltext = htmlfile.read()
htmlfile.close()

soup = BeautifulSoup(htmltext)

count = 0

movies = soup.findChildren('table','results')
itermovie = iter(movies[0].findChildren('tr'))
next(itermovie)

for tr in itermovie :
	imgSource = tr.findChildren('td','image')[0].find('img')['src'].split('._V1.')[0]+'_V1_SX214_AL.jpg'
	movie = tr.findChildren('td','title')
	title =movie[0].find('a').contents[0]+movie[0].find('span','year_type').contents[0]
	genres =movie[0].find('span','genre').findAll('a')
	genres =[g.contents[0] for g in genres]
	runtime = movie[0].find('span','runtime').contents[0]
	rating = movie[0].find('span','value').contents[0]

	print "IMDB Ratings"
	print "S No---->"
	count +=1
	print count
	print 'title -->'+title
	print 'genres-->',
	for item in genres:
			if genres.index(item) == len(genres)-1:
				print(item.decode('UTF-8','strict'))
			else:
				print(item.decode('UTF-8','strict'))
	print 'runtime-->'+runtime
	print 'rating-->'+rating
	print 'image source-->'+imgSource