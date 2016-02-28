import datetime

from django.shortcuts import render
from django_tables2 import RequestConfig

from .models import IzzyFlavor
from .tables import IzzyFlavorTable


def index(request):
    table = IzzyFlavorTable(IzzyFlavor.objects.filter(
        date_seen__date=datetime.date.today()))
    # paginate to show 32 flavors per page (1 page per location)
    RequestConfig(request, paginate={'per_page': 32}).configure(table)
    return render(request, 'scoops/index.html', {'table': table})


def flavor_detail(request, pk):
    flavor = IzzyFlavor.objects.get(pk=pk)
    return render(request, 'scoops/flavor_detail.html', {'flavor': flavor})
