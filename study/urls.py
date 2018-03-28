# study/urls.py

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.homeLV.as_view(), name='home'),
    url(r'^post/list/', views.postLV.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^agora/list/', views.agoraLV.as_view(), name='agora_list'),
    url(r'^agora/(?P<pk_2>\d+)/$', views.agora_detail, name='agora_detail'),
    url(r'^agora/new/$', views.agora_new, name='agora_new'),
    url(r'^agora/(?P<pk_2>\d+)/edit/$', views.agora_edit, name='agora_edit'),
    url(r'^agora/(?P<pk_2>\d+)/remove/$', views.agora_remove, name='agora_remove'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^comment/(?P<pk>\d+)/edit/$', views.comment_edit, name='comment_edit'),
]
