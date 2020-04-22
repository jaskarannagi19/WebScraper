# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy


class WebSpider(scrapy.Spider):
    name = "web"
    start_urls = ['https://scholar.google.com/']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(response,formxpath="//form[@id='gs_hdr_frm']",formdata={'q':'G. Brewka'},callback=self.parse_caseStatus)

    def parse_caseStatus(self,response):
        print(response.text)
