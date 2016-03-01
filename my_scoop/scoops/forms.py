from django.forms import ModelForm
from .models import FlavorReview


class FlavorReviewForm(ModelForm):
    class Meta:
        model = FlavorReview
        fields = ('review_title', 'flavor_rating', 'review_text')
