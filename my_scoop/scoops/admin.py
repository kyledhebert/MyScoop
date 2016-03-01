from django.contrib import admin

from scoops.models import IzzyFlavor, FavoriteFlavor, FlavorReview


class IzzyFlavorAdmin(admin.ModelAdmin):
    model = IzzyFlavor
    list_display = ('flavor_name', 'flavor_description', 'location',
                    'date_seen')


class FavoriteFlavorAdmin(admin.ModelAdmin):
    model = FavoriteFlavor
    list_display = ('user', 'flavor')


class FlavorReviewAdmin(admin.ModelAdmin):
    model = FlavorReview
    list_display = ('review_title', 'flavor_rating')

admin.site.register(IzzyFlavor, IzzyFlavorAdmin)
admin.site.register(FavoriteFlavor, FavoriteFlavorAdmin)
admin.site.register(FlavorReview, FlavorReviewAdmin)
