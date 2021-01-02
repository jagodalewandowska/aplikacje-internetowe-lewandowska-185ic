# powiązanie pomiędzy środowiskiem celery a projektem django tak,
# aby utworzyć instancję celery_app
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'image_parroter.settings')

celery_app = Celery('image_parroter')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()