from django.contrib import admin

from scoops.models import IzzyFlavor, FavoriteFlavor


class IzzyFlavorAdmin(admin.ModelAdmin):
    model = IzzyFlavor
    list_display = ('flavor_name', 'flavor_description', 'location',
                    'date_seen')


class FavoriteFlavorAdmin(admin.ModelAdmin):
    model = FavoriteFlavor
    list_display = ('user', 'flavor')    

admin.site.register(IzzyFlavor, IzzyFlavorAdmin)
admin.site.register(FavoriteFlavor, FavoriteFlavorAdmin)
