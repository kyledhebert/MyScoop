import scrapy
from scoopscraper.items import ScoopscraperItem


class IzzySpider(scrapy.Spider):
    name = "izzy_spider"
    allowed_domains = ["izzysicecream.com"]
    start_urls = (
        'http://flavorup.izzysicecream.com/flavor-grid/web/minneapolis',
    )
  
    def parse(self, response):
        item = ScoopscraperItem()
        for flavor in response.xpath('//*[@id="grid"]/ul/li'): 
            item['flavor_name'] = flavor.xpath('.//p[2]/text()').extract()
            item['flavor_description'] = flavor.xpath(
                './/div/p[2]/text()').extract()
            yield item
