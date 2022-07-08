import os
import socket
import tarfile
import logging
import inspect

from distutils.util import strtobool

from pathlib import Path

from django.conf import settings
from django.db.migrations.recorder import MigrationRecorder
from django.utils.dateparse import parse_datetime

from django_backup_utils.apps import BackupUtilsConfig
from django_backup_utils.exceptions import MigrationNotFound

logger = logging.getLogger(__name__)


def get_backup_name(filepath, hostname=None, projectname=None, all=False):
    if not isinstance(hostname, str) or len(hostname) == 0:
        hostname = socket.gethostname()
        logger.debug(f"set hostname to {hostname}")
    if not isinstance(projectname, str) or len(projectname) == 0:
        logger.debug(f"set projectname to {BackupUtilsConfig.PROJECT_NAME}")
        projectname = BackupUtilsConfig.PROJECT_NAME

    logger.debug(f"get_backup_name({filepath}, hostname={hostname}, projectname={projectname}, all={all})")
    splits = str(Path(filepath).name).split("_")
    logger.debug(f"splitted path: {splits}")

    if len(splits) == 4:
        splits_hostname = splits[0]
        splits_project = splits[1]

        if all:
            if str(filepath).endswith(".tar.gz") or str(filepath).endswith(".tar"):
                logger.debug(f"get_backup_name -> return {filepath}")
                return filepath

        if splits_hostname == hostname and splits_project == projectname:
            if str(filepath).endswith(".tar.gz") or str(filepath).endswith(".tar"):
                logger.debug(f"get_backup_name -> return {filepath}")
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
    logger.debug('get_migration_file_list()')
    f = MigrationRecorder.Migration.objects.all()
    migration_files = []
    not_found = []
    consistent = True
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
            logger.debug(f"missing migration: {each}")
            missing_migrations += str(each) + "\n"
        if not BackupUtilsConfig.BACKUP_IGNORE_CONSISTENCY:
            raise MigrationNotFound(missing_migrations)
        else:
            if (Path(str(inspect.getouterframes(inspect.currentframe())[1][1])).name) == 'createbackup.py':
                logger.warning(
                    f'some migration-files are missing, backup could be inconsistent missing:\n{missing_migrations}')
            consistent = False

    return migration_files, consistent


def extract_dumpinfo(tarpath):
    logger.debug(f"extract_dumpinfo({tarpath})")
    dump_info = tarfile.open(str(tarpath), "r")
    dump_info = dump_info.extractfile(f'{BackupUtilsConfig.DUMPINFO}').readlines()
    created_at = dump_info[0].decode("UTF-8").strip().split(";")[1]
    logger.debug(f'created_at: {created_at}')
    dump_version = dump_info[1].decode("UTF-8").strip().split(";")[1]
    logger.debug(f'dump_version: {dump_version}')
    system_migrations_migrated = dump_info[2].decode("UTF-8").strip().split(";")[1]
    logger.debug(f'system_migrations_migrated: {system_migrations_migrated}')
    dump_migration_files = dump_info[3].decode("UTF-8").strip().split(";")[1]
    logger.debug(f'dump_migration_files: {dump_migration_files}')
    consistent_migrations = strtobool(dump_info[4].decode("UTF-8").strip().split(";")[1])
    logger.debug(f'consistent_migrations: {consistent_migrations}')
    params = dump_info[5].decode("UTF-8").strip().split(";")[1]
    logger.debug(f'params: {params}')
    return {'created_at': created_at, "dump_version": dump_version,
            "system_migrations_migrated": system_migrations_migrated, "dump_migration_files": dump_migration_files,
            "params": params, 'consistent_migrations': consistent_migrations}


def get_backup_list_by_time(backup_root, hostname=None, projectname=None, all=False):
    files = os.listdir(backup_root)
    paths = [os.path.join(backup_root, basename) for basename in files]
    applicable = []
    d = {}
    if paths:
        for each in paths:
            backup = get_backup_name(each, hostname, projectname, all)
            if backup:
                d = {'path': backup, 'created_at': parse_datetime(extract_dumpinfo(Path(each)).get('created_at'))}
                applicable.append(d)
        sorted_list = sorted(applicable, key=lambda p: p["created_at"])
        latest = sorted_list[-1].get('path')
        return latest, sorted_list
    return None, None
