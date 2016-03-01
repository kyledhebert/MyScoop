from django.conf.urls import url

from . import views

app_name = 'scoops'
urlpatterns = [
    # ex: /scoops/13/
    url(r'^(?P<pk>[0-9]+)/$', views.flavor_detail,
        name='flavor_detail'),
    url(r'^(?P<flavor_id>[0-9]+)/add_to_favorites/$', views.add_to_favorites,
        name='add_to_favorites'),
    url(r'^(?P<flavor_id>[0-9]+)/remove_from_favorites/$',
        views.remove_from_favorites, name='remove_from_favorites'),
    url(r'^(?P<flavor_id>[0-9]+)/review_flavor/$',
        views.review_flavor, name='review_flavor'),
]
