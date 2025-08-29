"""
WSGI config for social_media_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

# Add your project directory to the sys.path
project_home = '/home/miraclejoseph/Alx_DjangoLearnLab/social_media_api'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variable for Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'social_media_api.settings'

# Activate your virtual environment
activate_env = '/home/miraclejoseph/Alx_DjangoLearnLab/social_media_api/venv/bin/activate_this.py'
with open(activate_env) as file_:
    exec(file_.read(), dict(__file__=activate_env))

# Get the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
