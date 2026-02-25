import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo/todo/settings.py")

app = get_wsgi_application()
