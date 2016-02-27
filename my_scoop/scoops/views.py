from django.shortcuts import render
from django_tables2 import RequestConfig

from .models import IzzyFlavor
from .tables import IzzyFlavorTable


def index(request):
    """Uses django_tables2 to render a table of flavors and locations"""
    # get a queryset of all flavors
    table = IzzyFlavorTable(IzzyFlavor.objects.all())
    # set to 32 flavors per page (1 page per location)
    RequestConfig(request, paginate={'per_page': 32}).configure(table)
    return render(request, 'scoops/index.html', {'table': table})


def flavor_detail(request, pk):
    # get the flavor by primary key
    flavor = IzzyFlavor.objects.get(pk=pk)
    return render(request, 'scoops/flavor_detail.html', {'flavor': flavor})
