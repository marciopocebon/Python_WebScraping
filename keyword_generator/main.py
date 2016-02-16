import gethtml
import articletext

url="www.nytimes.com/2016/02/15/sports/westminster-dog-show-judge-is-alone-on-center-stage.html"

article = articletext.getArticle(url)

print articletext.getKeywords(article)
