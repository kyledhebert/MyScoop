from scrapy.item import Item, Field


class ScoopscraperItem(Item):
    # Scraped Fields
    flavor_name = Field()
    flavor_description = Field()
    location = Field()

    # Calculated Field
    date_seen = Field()

    # Debug Field
    url = Field()
