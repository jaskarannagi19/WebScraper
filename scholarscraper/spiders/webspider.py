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
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        yield scrapy.FormRequest.from_response(response,formdata={'q':'G. Brewka'},callback=self.parse_caseStatus)

    def parse_caseStatus(self,response):
        print("-----------------------------------------------------------")
        print(response)
