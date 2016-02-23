from __future__ import unicode_literals

from django.db import models


class IzzyFlavor(models.Model):
    # Scraped Fields
    flavor_name = models.CharField(max_length=250)
    flavor_description = models.TextField()
    location = models.CharField(max_length=250)

    # Calculated Field
    date_seen = models.DateTimeField(auto_now_add=True)

    # Debug Field
    url = models.URLField(max_length=250)
