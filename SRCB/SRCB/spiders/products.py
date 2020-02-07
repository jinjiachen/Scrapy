# -*- coding: utf-8 -*-
import scrapy
from SRCB.items import SrcbItem

class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['srcb.com']
    start_urls = ['http://www.srcb.com/xyinvest/index.shtml']

    def parse(self, response):
        subselection=response.xpath("/vid[@class='xy_pro_content_t']").extract()
        items=[]
#        subselection.xpath("//td[@class='xy_tab_right xy_tab_left']//text()").extract() #product_name
#       subselection.xpath("//tbody/tr") #9个理财产品的块
        pass
