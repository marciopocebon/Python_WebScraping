from threading import Thread
import urllib
import re

def th(ur):
	regex = "<title>(.+?)</title>"
	pattern = re.compile(regex)
	htmltext = urllib.urlopen(ur).read()
	results = re.findall(pattern,htmltext)
	print results

urls = "http://google.com http://yahoo.com http://wikipedia.com http://cnn.com".split()

threadlist = []
for u in urls:
	t = Thread(target = th,args=(u,))
	t.start()
	threadlist.append(t)

for b in threadlist:
	b.join()
	

