from bs4 import BeautifulSoup
import gethtml

def getArticleText(webtext):
	articletext = ""
	soup = BeautifulSoup(webtext)
	for tag in soup.findAll('p',attrs={"class":"story-content"}):
		articletext += tag.contents[0]
	return articletext

def getArticle(url):
	htmltext = gethtml.getHtmlText(url)
	return getArticleText(htmltext)

def getKeywords(articletext):	
	word_dict ={}	
	word_list = articletext.lower().split()
	for word in word_list:
		if word not in word_list:
			word_dict[word] = 1
		if word in word_list:
			word_dict[word] +=1
		print word_dict
