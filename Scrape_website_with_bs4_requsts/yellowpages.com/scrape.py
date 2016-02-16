import requests
from bs4 import BeautifulSoup

url = "http://www.yellowpages.com/new-york-ny/coffee-shops"
r = requests.get(url)

#print r.content

soup = BeautifulSoup(r.content,"lxml")

#print soup.prettify()

#for link in soup.find_all('a'):
	#print link.get('href')
	#print link.text
	#print link.text ,link.get('href')
	#print "<a href='%s'>%s</a>" %(link.get("href"), link.text)
	
data = soup.find_all("div",{"class":"info"})
#print data
for item in data:
	#print item.text
	print item.contents[0].find_all("a",{"class":"business-name"})[0].text
	try:
		print item.contents[1].find_all("span",{"itemprop":"streetsAddress"})[0].text
	except:
		pass
	try:
		print item.contents[1].find_all("span",{"itemprop":"addressLocality"})[0].text.replace(',' ,'')
	except:
		pass
	try:
                print item.contents[1].find_all("span",{"itemprop":"addressRegion"})[0].text
        except: 
                pass
	try:
                print item.contents[1].find_all("span",{"itemprop":"postalCode"})[0].text        
        except:
                pass
	try:
                print item.contents[1].find_all("div",{"class":"primary"})[0].text        
        except:
                pass

