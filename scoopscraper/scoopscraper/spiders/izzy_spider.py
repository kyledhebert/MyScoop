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

            # declare input processors
            loader.flavor_description_in = MapCompose(unicode.strip)
            loader.flavor_name_in = MapCompose(unicode.strip)
            loader.location_in = MapCompose(unicode.strip)

            # default output processor
            loader.default_output_processor = Join()

            loader.add_xpath('flavor_name', './/p[2]/text()')
            loader.add_xpath(
                'flavor_description',
                './/div/p[2]/text()')
            loader.add_xpath(
                'location',
                '//*[@id="heading"]/h2/text()',
                # use regex to extract the location name from the <h2>
                # HTML: <h2>Current Flavors at Minneapolis</h2>
                re='(St\. Paul|Minneapolis)')
            # url captured for debug purposes
            loader.add_value('url', response.url)
            yield loader.load_item()
