"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os,sys
sys.path.append('C:/Users/user/upgrade_Aulmaru/mysite')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()


from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
