from pathlib import Path

from django.apps import AppConfig
from django.conf import settings


class BackupUtilsConfig(AppConfig):
    name = 'django_backup_utils'
    PROJECT_NAME = Path(settings.BASE_DIR).name
    JSON_FILENAME = 'django-backup-utils-fullbackup.json'
    DUMPINFO = 'django-backup-utils-backup-info.txt'
