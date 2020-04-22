# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy


class WebSpider(scrapy.Spider):
    name = "web"

    def start_requests(self):
        urls = [
            'https://scholar.google.com/',
        ]
        for url in urls:
            print("xxxxxxxxxxxxxxxxxxxxxxx")
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        request = scrapy.FormRequest.from_response(
            response,
            formxpath="//form[@id='gs_hdr_frm']",
	    formdata={
		'gs_hdr_tsi':'G. Brewka'
		},
            callback=self.parse_caseStatus
        )
        print(request.body)
        yield request

    def parse_caseStatus(self,response):
        print("---------------------------------------")
        print(response)
