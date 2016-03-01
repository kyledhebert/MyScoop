import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django_tables2 import RequestConfig

from .models import IzzyFlavor, FavoriteFlavor
from .tables import IzzyFlavorTable
from .forms import FlavorReviewForm


def index(request):
    table = IzzyFlavorTable(IzzyFlavor.objects.filter(
        date_seen__date=datetime.date.today()))
    # paginate to show 32 flavors per page (1 page per location)
    """Uses django_tables2 to render a table of flavors and locations"""
    # get a queryset of all flavors
    table = IzzyFlavorTable(IzzyFlavor.objects.all())
    # set to 32 flavors per page (1 page per location)
    RequestConfig(request, paginate={'per_page': 32}).configure(table)
    return render(request, 'scoops/index.html', {'table': table})


def flavor_detail(request, pk):
    # get the flavor by primary key
    flavor = IzzyFlavor.objects.get(pk=pk)
    user = request.user    
    
    def is_favorite(flavor, user):
        """Determines if the user has added this flavor to their favorites"""
        try:
            favorite = FavoriteFlavor.objects.filter(
                flavor_id=flavor.id).filter(user_id=user.id)
        except FavoriteFlavor.DoesNotExist, e:
            raise e
        # if the query has a value, then the user has marked this
        # flavor as a favorite    
        if (favorite):
            is_favorite = True
        else:
            is_favorite = False
        # determines whether "add to" or "remove from" favorites is shown    
        return is_favorite            

    return render(request, 'scoops/flavor_detail.html',
                  {'flavor': flavor,
                   'is_favorite': is_favorite(flavor, user)})


def add_to_favorites(request, flavor_id):
    # get the flavor being favorited
    flavor = IzzyFlavor.objects.get(pk=flavor_id)
    # create a new FavoriteFlavor entry and save it
    favorite = FavoriteFlavor(user=request.user, flavor=flavor)
    favorite.save()
    # redirect back to the current flavors list
    return HttpResponseRedirect(reverse('home'))


def remove_from_favorites(request, flavor_id):    
    # get the favorite being removed
    favorites = FavoriteFlavor.objects.filter(
        user_id = request.user.id
        ).filter(flavor_id=flavor_id)
    # loop over the query set and delete the item
    # should only return one
    for favorite in favorites:
        favorite.delete()
    # redirect back to the current flavors list
    return HttpResponseRedirect(reverse('home'))


def review_flavor(request, flavor_id):
    # get the flavor being reviewed 
    flavor = IzzyFlavor.objects.get(pk=flavor_id)
    # if this is a POST request, process the form data
    if request.method == 'POST':
        # populate the form with the submitted data
        form = FlavorReviewForm(request.POST)
        if form.is_valid():
            # create a new review, but don't save it yet
            new_review = form.save(commit=False)
            # we need to add the flavor and user ids to the review
            new_review.flavor = flavor
            new_review.author = request.user
            # now we can save the review
            new_review.save()
            # and send the user back to the flavor detail page
            return redirect('scoops:flavor_detail', pk=flavor.id)
    # if not a POST request, create a blank form
    else:
        form = FlavorReviewForm()

    return render(request, 'scoops/review_flavor.html', {
        'form': form, 'flavor': flavor})    
