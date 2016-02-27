from django.shortcuts import render
from django_tables2 import RequestConfig

from .models import IzzyFlavor
from .tables import IzzyFlavorTable


def index(request):
    table = IzzyFlavorTable(IzzyFlavor.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'scoops/index.html', {'table': table})


def flavor_detail(request, pk):
    flavor = IzzyFlavor.objects.get(pk=pk)
    return render(request, 'scoops/flavor_detail.html', {'flavor': flavor})
