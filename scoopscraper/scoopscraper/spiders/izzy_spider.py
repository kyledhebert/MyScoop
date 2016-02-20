from datetime import datetime

from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, MapCompose
from scrapy.spiders import Spider

from scoopscraper.items import ScoopscraperItem


class IzzySpider(Spider):
    """Spider for the current flavors page of izzysicecream.com"""
    name = "izzy_spider"
    allowed_domains = ["izzysicecream.com"]
    start_urls = [
        'http://flavorup.izzysicecream.com/flavor-grid/web/stpaul',
        'http://flavorup.izzysicecream.com/flavor-grid/web/minneapolis',
    ]

    # the starting xpath for flavors grid
    flavor_grid_xpath = '//*[@id="grid"]/ul/li'

    def parse(self, response):
        """Parses the current flavors grid.
        @url http://flavorup.izzysicecream.com/flavor-grid/web/stpaul
        @returns items 1
        @scrapes flavor_name flavor_description date_seen url 
        """
        # iterate over the flavors in the response using an ItemLoaded
        for flavor in response.xpath(self.flavor_grid_xpath):
            loader = ItemLoader(item=ScoopscraperItem(), selector=flavor)
            loader.add_xpath('flavor_name', './/p[2]/text()')
            loader.add_xpath(
                'flavor_description',
                './/div/p[2]/text()', MapCompose(unicode.strip),
                # join the <p> contents into a single entry
                Join())
            loader.add_value('date_seen', datetime.now())
            # url captured for debug purposes
            loader.add_value('url', response.url)
            yield loader.load_item()
