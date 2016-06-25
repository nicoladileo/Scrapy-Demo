from scrapy import Spider
from scrapy.selector import Selector
from stack.items import StackItem
import codecs

class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]

    def __init__(self, url_file = None, *args, **kwargs):
	super(StackSpider, self).__init__(*args, **kwargs)
        with codecs.open(url_file,'r','utf-8') as f:
		self.start_urls = f.readlines()

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]')
	
        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                'h3/a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'h3/a[@class="question-hyperlink"]/@href').extract()[0]
	    item['username'] = question.xpath(
		'.//div[@class="user-details"]/a/text()').extract()[0]
            item['useraddress'] = question.xpath(
		'.//div[@class="user-details"]/a/@href').extract()[0]
            yield item

