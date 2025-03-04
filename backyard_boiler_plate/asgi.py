# -*- coding: utf-8 -*-
"""
ASGI config for backyard_boiler_plate project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backyard_boiler_plate.settings")

application = get_asgi_application()
