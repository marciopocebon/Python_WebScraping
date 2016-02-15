import urllib
import json
import re

htmlfile = urllib.urlopen('http://www.cricbuzz.com/api/match/current')
#htmltext = htmlfile.read()

data = json.load(htmlfile)

names = data[0]

print names
