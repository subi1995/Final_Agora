# study/urls.py

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.homeLV.as_view(), name='home'),
    url(r'^agora/list/', views.agoraLV.as_view(), name='agora_list'),
    url(r'^agora/(?P<pk_2>\d+)/$', views.agora_detail, name='agora_detail'),
    url(r'^agora/new/$', views.agora_new, name='agora_new'),
    url(r'^agora/(?P<pk_2>\d+)/edit/$', views.agora_edit, name='agora_edit'),
    url(r'^agora/(?P<pk_2>\d+)/remove/$', views.agora_remove, name='agora_remove'),    
]
