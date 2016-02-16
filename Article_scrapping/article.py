import mechanize
from bs4 import BeautifulSoup
br = mechanize.Browser()
htmlfile = br.open("http://www.nytimes.com/2016/02/15/sports/westminster-dog-show-judge-is-alone-on-center-stage.html")
#print htmltext.read()

htmltext = htmlfile.read()

articletext = ""
soup = BeautifulSoup(htmltext,"lxml")
for tag in soup.findAll('p',attrs={"class":"story-content"}):
	articletext += tag.contents[0]
	print articletext
