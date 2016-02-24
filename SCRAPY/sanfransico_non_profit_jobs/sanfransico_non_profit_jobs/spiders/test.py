from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from sanfransico_non_profit_jobs.items import SanfransicoNonProfitJobsItem

class MySpider(BaseSpider):
	"""docstring for MySpider"""
	name = "kiran"
	allowed_domains= ["craigslist.org"]
	start_urls = ["http://sfbay.craigslist.org/sfc/npo"]

	def parse(self, response):
		hxs =HtmlXPathSelector(response)
		titles = hxs.select("//*/div[2]/div[3]/span/p")
		items = []

		for titles in titles:
			item = SanfransicoNonProfitJobsItem()
			titles ["title"]= titles.select("a/text()").extract()
			link ["link"]= titles.select("a/@href").extract()
			item.append(item)
		return items