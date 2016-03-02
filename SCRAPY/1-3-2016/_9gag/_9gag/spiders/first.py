# -*- coding: utf-8 -*-
import scrapy
from _9gag.items import GagItem

class FirstSpider(scrapy.Spider):
    name = "first"
    allowed_domains = ["9gag.com"]
    start_urls = (
        'http://www.9gag.com/',
    )
    
    last_gag_id = None
    def parse(self, response):
    	count = 0
        for article in response.xpath('//article'):
            gag_id = article.xpath('@data-entry-id').extract()
            count +=1
            if gag_id:
            	if (count != 100):
                	last_gag_id = gag_id[0]
                	ninegag_item = GagItem()
                	ninegag_item['entry_id'] = gag_id[0]
                	ninegag_item['url'] = article.xpath('@data-entry-url').extract()[0]
                	ninegag_item['votes'] = article.xpath('@data-entry-votes').extract()[0]
                	ninegag_item['comments'] = article.xpath('@data-entry-comments').extract()[0]
                	ninegag_item['title'] = article.xpath('.//h2/a/text()').extract()[0].strip()
                	ninegag_item['img_url'] = article.xpath('.//div[1]/a/img/@src').extract()

                	yield ninegag_item
                	
                	
                else:
                	break
                
        
        next_url = 'http://9gag.com/?id=%s&c=200' % last_gag_id
        yield scrapy.Request(url=next_url, callback=self.parse)	
        print count


