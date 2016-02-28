import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
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


def add_to_favorites(request, flavor_id):
    # get the flavor being favorited
    flavor = IzzyFlavor.objects.get(pk=flavor_id)
    # add the user to the flavor's favorited_by field
    user = User.objects.get(pk=request.user.id)
    flavor.favorited_by.add(user)
    # save the flavor
    flavor.save()
    # redirect back to the current flavors list
    return HttpResponseRedirect(reverse('home'))
