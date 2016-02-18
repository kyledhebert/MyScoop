from scrapy.item import Item, Field


class ScoopscraperItem(Item):
    # Primary Fields
    flavor_name = Field()
    flavor_description = Field()
    date_seen = Field()

    # Debug Fields
    url = Field()
