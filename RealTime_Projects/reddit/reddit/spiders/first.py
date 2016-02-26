# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from reddit.items import RedditItem

class FirstSpider(CrawlSpider):
    name = "first"
    allowed_domains = ["www.reddit.com"]
    start_urls = ['https://www.reddit.com/r/pics',
    ]

    rules =[
    	Rule(LinkExtractor(
    		allow=['/r/pics/\?count=\d*&after=\w*']),
    		callback='parse_item',
    		follow=True),
    	]

    def parse_item(self, response):
        
        selector_list = response.css('div.thing')

        for selector in selector_list:
        	item = RedditItem()
        	item['image_urls'] = selector.xpath('a/@href').extract()
        	item['title'] = selector.xpath('div/p/a/text()').extract()
        	item['url'] = selector.xpath('a/@href').extract()

        	yield item
