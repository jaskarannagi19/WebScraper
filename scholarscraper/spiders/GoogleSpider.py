# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from scrapy.http import Request

class GoogleSpider(scrapy.Spider):
    name = "google"
    start_urls = ['https://scholar.google.com/']
    BASE_URL = 'https://scholar.google.com'

    def parse(self, response):
        '''First function called for to yield results'''
        if hasattr(self, 'author'):
            yield scrapy.FormRequest.from_response(response,formxpath="//form[@id='gs_hdr_frm']",formdata={'q':self.author},callback=self.parse_caseAuthor)

        if hasattr(self, 'title'):
            yield scrapy.FormRequest.from_response(response, formxpath="//form[@id='gs_hdr_frm']",formdata={'q': self.title}, callback=self.citation_score)

    def parse_caseAuthor(self,response):
        '''Extracts the author url from name page'''
        author_url = response.xpath('//h4[@class="gs_rt2"]/a/@href').get()
        print(response.xpath('//h4[@class="gs_rt2"]/a/@href').get())
        yield Request(url=self.BASE_URL+author_url, callback=self.author_profile)

    def author_profile(self,response):
        '''Extract h-index of author form profile'''
        print(response.xpath('//table[@id="gsc_rsb_st"]//tr[2]//td[2]/text()').get())
        return response.xpath('//table[@id="gsc_rsb_st"]//tr[2]//td[2]/text()').get()

    def citation_score(self,response):
        '''Extract citation score of the first link'''
        print(response.xpath('//div[@class="gs_fl"]//a/text()').get())
        return response.xpath('//div[@class="gs_fl"]//a/text()').get()