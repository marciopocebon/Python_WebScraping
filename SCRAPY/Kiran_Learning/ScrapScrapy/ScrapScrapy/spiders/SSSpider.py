from scrapy.selector import Selector
from scrapy.spiders import BaseSpider
from ScrapScrapy.items import ScrapscrapyItem

class ScrapyscrapSpider (BaseSpider) :
  name = "ss"
  allowed_domains = ["scrapy.org"]
  start_urls = ['http://scrapy.org/']

  def parse(self, response) :
    sel = Selector (response)
    item = ScrapscrapyItem ()
    item['Heading'] = str (sel.xpath ('//*[@id="scrapy-logo"]').extract())
    item['Content'] = str (sel.xpath ('/html/body/div[2]/div/div[1]/div/div[1]/p/text()').extract ())
    item['Source_Website'] = "http://scrapy.org"
    return item

##To run 
## scrapy crawl ss
## IN the base folder

