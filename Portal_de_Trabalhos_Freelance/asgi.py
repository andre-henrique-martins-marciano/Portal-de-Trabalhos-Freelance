"""
ASGI config for Portal_de_Trabalhos_Freelance project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portal_de_Trabalhos_Freelance.settings')

application = get_asgi_application()
