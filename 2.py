import urllib
import re

urls =["http://google.com","http://nytimes.com","http://CNN.com"]

i = 0

regex = '<title>(.+?)</title>'
pattern = re.compile(regex)
while i< len(urls):
	htmlfile = urllib.urlopen(urls[i])
	htmltext = htmlfile.read()
	#print htmltext
	#print html[0:100] #first 100
	titles = re.findall(pattern,htmltext)
	print titles 
	i+=1
