import os
from pathlib import Path

import pkg_resources
from django.apps import AppConfig
from django.conf import settings
from django.db.models import BigAutoField


class BackupUtilsConfig(AppConfig):
    name = 'django_backup_utils'
    PROJECT_NAME = Path(settings.BASE_DIR).name
    JSON_FILENAME = 'django-backup-utils-fullbackup.json'
    DUMPINFO = 'django-backup-utils-backup-info.txt'
    DJANGO_BACKUP_UTILS_VERSION = str(pkg_resources.get_distribution('django-backup-utils').version)
    DEFAULT_AUTO_FIELD = BigAutoField

    try:
        BACKUP_IGNORE_CONSISTENCY = settings.BACKUP_IGNORE_CONSISTENCY
    except AttributeError:
        BACKUP_IGNORE_CONSISTENCY = False

    try:
        BACKUP_DIRS = settings.BACKUP_DIRS
    except AttributeError:
        BACKUP_DIRS = []

    if BACKUP_DIRS:
        for each in BACKUP_DIRS:
            if not Path(os.path.commonprefix([Path(each), Path(settings.BASE_DIR)])) == Path(settings.BASE_DIR):
                raise Exception(f"BACKUP_DIRS path {each} needs to be relative to settings.BASE_DIR ")
