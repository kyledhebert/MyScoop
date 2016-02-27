from django.conf.urls import url

from . import views

app_name = 'scoops'
urlpatterns = [
    # ex: /scoops/13/
    url(r'^(?P<pk>[0-9]+)/$', views.flavor_detail,
        name='flavor_detail_view'),
]
