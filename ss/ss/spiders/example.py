# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/Alvin9999/new-pac/wiki/ss%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7']

    def parse(self, response):
        ss=response.xpath("//div[@class='markdown-body']/p")[22].extract()
        with open ("ss.txt",'w+') as f:
            f.write(ss)
            f.close()
        pass
