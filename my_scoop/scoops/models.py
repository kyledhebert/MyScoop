from __future__ import unicode_literals

from django.contrib.auth.models import User
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


class FavoriteFlavor(models.Model):
    user = models.ForeignKey(User, unique=False)
    flavor = models.ForeignKey(
        IzzyFlavor, unique=False, on_delete=models.CASCADE)


class FlavorReview(models.Model):
    flavor = models.ForeignKey(IzzyFlavor)
    author = models.ForeignKey(User)
    review_title = models.CharField(max_length=250)
    RATING_CHOICES = (
        (1, "1 Star"),
        (2, "2 Stars"),
        (3, "3 Stars"),
        (4, "4 Stars"),
    )
    flavor_rating = models.CharField(max_length=1, choices=RATING_CHOICES)
    review_text = models.TextField()
