import urllib
import re

symbolslist = ["appl","spy","goog","nflx"]

i=0
while i<len(symbolslist):
	url ="http://in.finance.yahoo.com/q?s=" +symbolslist[i] +"&ql=1"
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()
	regex ='<span id="yfs_l84_[^.]*">(.+?)</span>' 
	pattern = re.compile(regex)
	print regex
	price = re.findall(pattern,htmltext)
	print "price of ",symbolslist[i],"is",price
	i+=1
	

	
