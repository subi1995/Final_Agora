from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reservation/$',views.reservationLV.as_view(), name = 'Room_Reservation'),
    url(r'^reservation/(?P<pk_2>\d+)/$', views.reservation_detail, name='reservation_detail'),
    url(r'^reservation/new/$', views.reservation_new, name = 'reservation_new'),
    url(r'^reservation/(?P<pk_2>\d+)/remove/$', views.reservation_remove, name='reservation_remove'),
    url(r'^reservation/(?P<pk_2>\d+)/edit/$', views.reservation_edit, name='reservation_edit'),
]
