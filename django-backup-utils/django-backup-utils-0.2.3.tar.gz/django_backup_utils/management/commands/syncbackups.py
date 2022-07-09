import logging
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from django_backup_utils.helpers import get_backup_list_by_time, synchronize_backups

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--silent', action='store_true', help="mutes some output")

    def handle(self, silent, *args, **options):
        if os.path.exists(settings.BACKUP_ROOT):
            sorted_backups = get_backup_list_by_time(settings.BACKUP_ROOT)
            if not sorted_backups:
                print("no backups found")
            else:
                synclist = synchronize_backups(sorted_backups)
                for each in synclist:
                    logger.debug(f"synchronized {each.__dict__}")
                    if not silent:
                        print(f"synchronized {each.backup} -> {each}")
        else:
            print(f"no backups have been created yet")
