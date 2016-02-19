import urllib
from bs4 import BeautifulSoup

film_name ="Deadpool_(film)"

url ="https://en.wikipedia.org/wiki/"+film_name
htmlfile = urllib.urlopen(url)
htmltext = htmlfile.read()

soup = BeautifulSoup(htmltext,"lxml")
#print soup.prettify()
movie_title = soup.find('h1',{'id':'firstHeading'})
print movie_title.text

'''Find all p tags in content'''
movie_info = soup.find_all('p')

'''Function used to find next sibling of a given element'''
def findNextSibling(resultant_url):
    return resultant_url.next_sibling

'''Function used to print the text in the current tag if 
	it is a p tag otherwise if it is h2 the loop will break
	and if no such element found error occurs'''
def content(resultant_url2,title):
	for _ in range(15):
	    try:
	            resultant_url2 = findNextSibling(resultant_url2)
	            if(resultant_url2.name == 'p'): #or resultant_url2.name ==div):
	                    print resultant_url2.text
	            elif(resultant_url2.name == 'h2' or resultant_url2.name =='div'):
	            		print "End of "+title
	            		break
	            else:
	                    pass
	    except:
	            print "error"


resultant_url = movie_info[0]
title = movie_info[0].text

'''Title'''
content(resultant_url,title)

'''Find all Heading in the content
   And also printing the entire headings
   in the body'''
h2tag = soup.find_all('h2')
for each_h2_tag in h2tag:
	print each_h2_tag.text

'''Take the first h2 tag and scrape its siblings upto next
	occurence of h2 tag using the function call'''

for _ in range(len(h2tag)):
	resultant_url2 = h2tag[1]
	title = h2tag[1].text
	print h2tag[1].text
	content(resultant_url2,title)
'''
Cast-Data
'''
resultant_url3 = h2tag[2]
title = h2tag[2].text
print h2tag[2].text
content(resultant_url3,title)


'''
Development
'''
resultant_url3 = h2tag[3]
title = h2tag[3].text
print h2tag[3].text
content(resultant_url3,title)

