import os
from django.core.wsgi import get_wsgi_application

# Replace 'todo.settings' with your actual project settings path
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo.settings")

app = get_wsgi_application()