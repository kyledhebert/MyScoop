from scrapy_djangoitem import DjangoItem

from scoops.models import IzzyFlavor


class ScoopscraperItem(DjangoItem):
    django_model = IzzyFlavor
