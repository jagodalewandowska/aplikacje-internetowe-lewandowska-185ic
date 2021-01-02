# sprawienie, że aplikacja skonfigurowana będzie włączana
# kiedy przy starcie aplikacji django 

from .celery import celery_app

__all__ = ('celery_app',)