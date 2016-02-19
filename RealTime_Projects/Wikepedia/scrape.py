import urllib
from bs4 import BeautifulSoup

film_name ="Deadpool_(film)"

url ="https://en.wikipedia.org/wiki/"+film_name
htmlfile = urllib.urlopen(url)
htmltext = htmlfile.read()

soup = BeautifulSoup(htmltext,"html.parser")
#print soup.prettify()
'''Title'''
movie_title = soup.find('h1',{'id':'firstHeading'})
#print movie_title.text

'''Find all p tags in content'''
movie_info = soup.find_all('p')

'''Function used to find next sibling of a given element'''
def findNextSibling(resultant_url):
	return resultant_url.next_sibling

'''Function used to print the text in the current tag if 
	it is a p tag otherwise if it is h2 the loop will break
	and if no such element found error occurs'''
def content(resultant_url2,title):
	while True :
		# resultant_url2 = findNextSibling(resultant_url2)
		resultant_url2 = resultant_url2.next_sibling
		try:
			if(resultant_url2.name == 'p'): 
				print resultant_url2.text
				print "P tag"
				
			elif(resultant_url2.name == 'h3'):
				print "H3 tag"
				print resultant_url2.text
				
			elif(resultant_url2.name == 'h4'):
				print resultant_url2.text
				print "h4 tag"
				
			elif(resultant_url2.name == 'table'):
				print "Unwanted Tag- table"
			elif(resultant_url2.name == 'div'):
				print "Unwanted Tag div"
			elif(resultant_url2.name == 'ul'):
				print "Unwanted Tag ul"
			elif(resultant_url2.name == 'dl'):
				print "Unwanted Tag dl"
			elif(resultant_url2.name == None):
				print "Unwanted Tag no tag"
				
			elif(resultant_url2.name == 'h2'):
				print "End of "+title
				break
			else:
				pass
		except:
			# print "error"
		
'''Find all Heading in the content
   And also printing the entire headings
   in the body'''
h2tag = soup.find_all('h2')

'''Take the first h2 tag and scrape its siblings upto next
	occurence of h2 tag using the function call'''


resultant_url2 = h2tag[3]
title =h2tag[3].text
print resultant_url2

content(resultant_url2,title)
for i in range(len(h2tag)-1):
	i = i+1
	resultant_url2 = h2tag[i]
	title = h2tag[i].text
	print h2tag[i].text
	content(resultant_url2,title)
