# mysite/urls.py
from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from study import views 


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^', include('study.urls', namespace='study')), #, namespace='study'
    url(r'^',include('reservation.urls')),
    url(r'^accounts/signup/$', views.signup, name='signup'),
	url(r'^summernote/', include('django_summernote.urls')),
]

if settings.DEBUG: # setting.py의 DEBUG = True인 경우
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
