# __init__.py in your project folder

from .celery import app as celery_app

__all__ = ('celery_app',)
