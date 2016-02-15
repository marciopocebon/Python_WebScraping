import urllib
import re

url ="http://www.google.com/finance/getprices?q=AAPL&x=NASD&i=120&p=25m&f=c&df=cpct&auto=1"
htmltext = urllib.urlopen(url).read()

print htmltext.split()[len(htmltext.split())-1]

