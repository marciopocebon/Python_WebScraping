import urllib
from bs4 import BeautifulSoup

url ="https://en.wikipedia.org/wiki/Deadpool_(film)"
htmlfile = urllib.urlopen(url)
htmltext = htmlfile.read()

soup = BeautifulSoup(htmltext,"lxml")
#print soup.prettify()
movie_title = soup.find('h1',{'id':'firstHeading'})
print movie_title.text

movie_info = soup.find_all('p')
# print movie_info[0].text
# print movie_info[1].text


resultant_url = movie_info[0]

def findNextSibling(resultant_url):
    #tag_addition = 'next_sibling'
    #base_url.string = base_url.string + '.' + tag_addition
    return resultant_url.next_sibling


for _ in range(40):
    try:
            resultant_url = findNextSibling(resultant_url)
            if(resultant_url.name == 'p'):
                    print resultant_url.text
            elif(resultant_url.name == 'h2'):
            		print "End of Introduction"
              		break
            else:
                    pass
    except:
            print "error"



h2tag = soup.find_all('h2')

resultant_url2 = h2tag[1]
title = h2tag[1].text
print h2tag[1].text


def content(resultant_url2,title):
	for _ in range(40):
	    try:
	            resultant_url2 = findNextSibling(resultant_url2)
	            if(resultant_url2.name == 'p'):
	                    print resultant_url2.text
	            elif(resultant_url2.name == 'h2'):
	            		print "End of "+title
	            		break
	            else:
	                    pass
	    except:
	            print "error"

content(resultant_url2,title)

resultant_url2 = h2tag[2]
title = h2tag[2].text
print h2tag[2].text
content(resultant_url2,title)



