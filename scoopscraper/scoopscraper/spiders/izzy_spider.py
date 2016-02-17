# -*- coding: utf-8 -*-
import scrapy


class IzzySpiderSpider(scrapy.Spider):
    name = "izzy_spider"
    allowed_domains = ["izzysicecream.com"]
    start_urls = (
        'http://www.izzysicecream.com/',
    )

    def parse(self, response):
        pass
