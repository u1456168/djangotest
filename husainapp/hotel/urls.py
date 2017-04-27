from django.conf.urls import url
from hotel import views as hotel_views
app_name = 'hotel'
urlpatterns = [
    #url(r'^$',hotel_views.index, name='index'),
    url(r'^categories/(?P<pk>[0-9]+)$', hotel_views.hoteldetails, name='hoteldetails'),
    url(r'^categories/create$', hotel_views.hotelcreate, name='hotelcreate'),
]
