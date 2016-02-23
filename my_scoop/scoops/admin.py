from django.contrib import admin

from scoops.models import IzzyFlavor


class IzzyFlavorAdmin(admin.ModelAdmin):
    model = IzzyFlavor
    list_display = ('flavor_name', 'flavor_description', 'location',
                    'date_seen')

admin.site.register(IzzyFlavor, IzzyFlavorAdmin)
