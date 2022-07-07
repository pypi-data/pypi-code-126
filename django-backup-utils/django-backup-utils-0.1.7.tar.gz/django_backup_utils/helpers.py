import os
import socket
import tarfile
import logging

from pathlib import Path

from django.conf import settings
from django.db.migrations.recorder import MigrationRecorder

from django_backup_utils.apps import BackupUtilsConfig
from django_backup_utils.exceptions import MigrationNotFound

logger = logging.getLogger(__name__)


def get_backup_name(filepath, hostname=None, projectname=None, all=False):
    if not isinstance(hostname, str):
        hostname = socket.gethostname()
    if not isinstance(projectname, str):
        projectname = BackupUtilsConfig.PROJECT_NAME

    splits = str(Path(filepath).name).split("_")

    if len(splits) == 4:
        splits_hostname = splits[0]
        splits_project = splits[1]

        if all:
            if str(filepath).endswith(".tar.gz") or str(filepath).endswith(".tar"):
                return filepath

        if splits_hostname == hostname and splits_project == projectname:
            if str(filepath).endswith(".tar.gz") or str(filepath).endswith(".tar"):
                return filepath


def get_system_migrations():
    f = MigrationRecorder.Migration.objects.all()
    unique_migration_dirs = set()
    system_migrations_migrated = 0
    system_migrations_files = 0

    for each in f.order_by('applied'):
        if Path(f"{settings.BASE_DIR}/{each.app}").is_dir():
            system_migrations_migrated += 1
            unique_migration_dirs.add(Path(f"{settings.BASE_DIR}/{each.app}"))

    for each in unique_migration_dirs:
        if Path(f"{each}/migrations/__init__.py").exists():
            for file in os.listdir(f"{each}/migrations/"):
                if file.endswith(".py") and not file.startswith('__init__'):
                    system_migrations_files += 1

    return system_migrations_migrated, system_migrations_files


def get_migration_file_list():
    f = MigrationRecorder.Migration.objects.all()
    migration_files = []
    not_found = []
    missing_migrations = ""
    for each in f.order_by('applied'):
        if Path(f"{settings.BASE_DIR}/{each.app}").is_dir():
            if Path(f"{settings.BASE_DIR}/{each.app}/migrations/__init__.py").is_file():
                path = Path(f"{settings.BASE_DIR}/{each.app}/migrations/{each.name}.py")
                migration_files.append(path)
                if not path.is_file():
                    not_found.append(str(path.relative_to(settings.BASE_DIR)))

    if not_found:
        for each in not_found:
            missing_migrations += str(each) + "\n"
        if not BackupUtilsConfig.BACKUP_IGNORE_CONSISTENCY:
            raise MigrationNotFound(missing_migrations)
        else:
            logger.warning(f'some migration-files are missing, backup could be inconsistent\n{missing_migrations}')

    return migration_files


def extract_dumpinfo(tarpath):
    dump_info = tarfile.open(str(tarpath), "r")
    dump_info = dump_info.extractfile(f'{BackupUtilsConfig.DUMPINFO}').readlines()
    created_at = dump_info[0].decode("UTF-8").strip().split(";")[1]
    system_version = dump_info[1].decode("UTF-8").strip().split(";")[1]
    dump_version = dump_info[2].decode("UTF-8").strip().split(";")[1]
    system_migrations_migrated = dump_info[3].decode("UTF-8").strip().split(";")[1]
    system_migration_files = dump_info[4].decode("UTF-8").strip().split(";")[1]
    params = dump_info[5].decode("UTF-8").strip().split(";")[1]
    return {'created_at': created_at, "system_version": system_version, "dump_version": dump_version,
            "system_migrations_migrated": system_migrations_migrated, "system_migration_files": system_migration_files,
            "params": params}
