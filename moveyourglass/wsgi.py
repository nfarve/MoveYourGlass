"""
WSGI config for moveyourglass project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moveyourglass.settings")

<<<<<<< HEAD
#from dj_static import Cling
=======
>>>>>>> 995adfcf7ccef34df3d63ba5ec0bcb62b2e52553

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
