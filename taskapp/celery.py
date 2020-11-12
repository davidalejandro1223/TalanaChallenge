"""Celery app config."""

# Utilities

import os
from celery import Celery

# Django
from django.apps import apps, AppConfig
from django.conf import settings

if not settings.configured:
    # configuracion de los settings de django a usar
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TalanaChallenge.settings') 


app = Celery('TalanaChallenge')
app.config_from_object('django.conf:settings', namespace='CELERY')


class CeleryAppConfig(AppConfig):
    name = 'taskapp'
    verbose_name = 'Celery Config'

    def ready(self):
        installed_apps = [app_config.name for app_config in apps.get_app_configs()]
        app.autodiscover_tasks(lambda: installed_apps, force=True)