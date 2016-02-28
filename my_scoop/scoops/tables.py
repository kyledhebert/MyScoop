import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor

from .models import IzzyFlavor


class IzzyFlavorTable(tables.Table):
    flavor_name = tables.LinkColumn('scoops:flavor_detail_view',
                                    args=[A('pk')],
                                    verbose_name="Flavor",)
    # flavor_description = tables.Column(verbose_name="Description")
    location = tables.Column(verbose_name="Location")
    
    class Meta:
        model = IzzyFlavor
        exclude = ('id', 'date_seen', 'url', 'flavor_description',)
