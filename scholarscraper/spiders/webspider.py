# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from scrapy.http import Request

class WebSpider(scrapy.Spider):
    name = "web"
    start_urls = ['https://scholar.google.com/']
    BASE_URL = 'https://scholar.google.com'

    def parse(self, response):
        yield scrapy.FormRequest.from_response(response,formxpath="//form[@id='gs_hdr_frm']",formdata={'q':'G. Brewka'},callback=self.parse_caseStatus)

    def parse_caseStatus(self,response):
        author_url = response.xpath('//h4[@class="gs_rt2"]/a/@href').get()
        #print(response.xpath('//h4[@class="gs_rt2"]/a/@href').get())
        yield Request(url=self.BASE_URL+author_url, callback=self.author_profile)
    def author_profile(self,response):
        #print(response.xpath('//table[@id="gsc_rsb_st"]//tr[2]//td[2]/text()').get())
        return response.xpath('//table[@id="gsc_rsb_st"]//tr[2]//td[2]/text()').get()

