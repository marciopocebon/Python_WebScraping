import urllib
import re

htmltext =urllib.urlopen("http://www.google.com/finance?q=AAPL").read()

regex ='<span id="ref_[^.]*_l">(.+?)</span>'
pattern = re.compile(regex)
results = re.findall(pattern,htmltext)

print results

