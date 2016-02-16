from threading import Thread
import urllib
import re

def th(ur):
	base = "http://finance.yahoo.com/q?s="+ur
	#regex = "<title>(.+?)</title>"
	regex ='<span id="yfs_l84_'+ur.lower()+'">(.+?)</span>'
	pattern = re.compile(regex)
	htmltext = urllib.urlopen(base).read()
	results = re.findall(pattern,htmltext)
	#print results
	print "the price of",ur,"is",results

symbolslist = open("symbollist.txt").read()
symbolslist = symbolslist.split("\n")

print symbolslist

threadlist = []

for u in symbolslist:
	t = Thread(target=th,args=(u,))
	t.start()
	threadlist.append(t)

for b in threadlist:
	b.join()
	

