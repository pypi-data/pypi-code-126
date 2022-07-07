import os
import sys
import json
import shutil
import logging
import tarfile
import unittest
import subprocess

from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from django_backup_utils import models
from django_backup_utils.tests import loaddata
from django_backup_utils.apps import BackupUtilsConfig
from django_backup_utils.helpers import get_migration_file_list, get_system_migrations, get_backup_name, \
    extract_dumpinfo
from django_backup_utils.exceptions import MigrationNotFound, LoadException, UnittestFailed

module = str(__name__).split(".")[-1]
logger = logging.getLogger(__name__)


def open_tar(input_filename):
    if str(input_filename).endswith("tar.gz"):
        tar = tarfile.open(input_filename, "r:gz")
    elif str(input_filename).endswith("tar"):
        tar = tarfile.open(input_filename, "r:")
    return tar


def extract_tar(input_filename, member_path="", dir="", strip=0, checkonly=False):
    tar = open_tar(input_filename)
    if member_path:
        for member in tar.getmembers():
            if member_path:
                if member_path in member.name:
                    if not strip <= 0:
                        p = Path(member.path)
                        member.path = p.relative_to(*p.parts[:strip])
                        logger.debug(member.path)
                    if not checkonly:
                        tar.extract(member, settings.BASE_DIR)
                        logger.debug(f"extracted {member.name} to {settings.BASE_DIR}")
    elif dir:
        for member in tar.getmembers():
            dir_member = []
            if member.name in dir:
                logger.debug(f"found BACKUP_DIR in backup {dir}")
                if not checkonly:
                    dir_member.append(member)
                    submembers = tar.getmembers()
                    for submember in submembers:
                        if str(submember.name).startswith(member.name):
                            dir_member.append(submember)
                    tar.extractall(members=dir_member, path=settings.BASE_DIR)
    tar.close()


def check_member(input_filename, member_path, strip=0):
    logger.debug(f"check for data in backup... {member_path}")
    tar = open_tar(input_filename)
    for member in tar.getmembers():
        if member.name in member_path:
            return member.name


def load_database_dump(filepath, **kwargs):
    logger.debug(f"loading backup fixture {filepath.name}...")
    command = f"{sys.executable} manage.py loaddata {filepath}"
    output = subprocess.getoutput(command)
    if not "Installed" in output:
        raise LoadException(message=f"load_database_dump has failed", output=output, **kwargs)
    else:
        logger.debug(output)


def flush_db():
    logger.debug("flushing db...")
    command = f"{sys.executable} {settings.BASE_DIR}/manage.py flush --noinput"
    output = subprocess.getoutput(command)
    logger.debug("db has been flushed")


def delete_dir(dir, **kwargs):
    dir = Path(dir)
    if dir.exists():
        shutil.rmtree(dir)
    if dir.exists():
        raise LoadException(message=f"directory could not be deleted", output=dir, **kwargs)
    else:
        logger.debug(f"deleted directory {dir}")


def latest_backup(backup_root):
    files = os.listdir(backup_root)
    paths = [os.path.join(backup_root, basename) for basename in files]

    applicable = []
    if paths:
        for each in paths:
            backup = get_backup_name(each)
            if backup:
                applicable.append(backup)
        return max(applicable, key=os.path.getctime)


def create_input():
    inp = input("continue y/N ? ")
    if str(inp) == "y" or str(inp) == "yes":
        return True


class Command(BaseCommand):

    def __init__(self):
        self.migrations = None
        self.migration_not_found = None
        try:
            self.migrations = get_migration_file_list()
        except MigrationNotFound as e:
            self.migration_not_found = e

        self.json_path = Path(os.path.join(settings.BASE_DIR, BackupUtilsConfig.JSON_FILENAME))
        self.dumpinfo_path = Path(os.path.join(settings.BASE_DIR, BackupUtilsConfig.DUMPINFO))
        self.system_migrations_migrated, self.system_migration_files = get_system_migrations()
        self.context = {'system_migrations_migrated': self.system_migrations_migrated}
        self.context['system_migration_files'] = None
        self.context['system_version'] = settings.BACKUP_SYSTEM_VERSION
        self.context['module'] = module
        super(Command, self).__init__()

    def add_arguments(self, parser):
        parser.add_argument('--tarpath', type=str, help='load the specified backup tarfile')
        parser.add_argument('--flush', action='store_true', help='flush the database (delete existing data)')
        parser.add_argument('--deletedirs', action='store_true',
                            help='delete all directories specified in settings.BACKUP_DIRS (before restoring)')
        parser.add_argument('--noinput', action='store_true', help='disable all prompts')
        parser.add_argument('--loadmigrations', action='store_true', help='restore all migration files')
        parser.add_argument('--skiptest', action='store_true', help='skip the unittest for loading database dump')
        parser.add_argument('--silent', action='store_true', help='mutes some output')

    def handle(self, tarpath, flush, deletedirs, noinput, loadmigrations, skiptest, silent, *args, **options):

        params = json.dumps(
            {"flush": flush, "deletedirs": deletedirs, "noinput": noinput, "loadmigrations": loadmigrations,
             "skiptest": skiptest, 'silent': silent})
        self.context['params'] = params

        if not tarpath:
            tar = latest_backup(settings.BACKUP_ROOT)
            if tar:
                tarpath = Path(tar)
                if not silent:
                    print(f"loading latest backup: {tarpath}, {tarpath.stat().st_size / 1000 / 1000} MB")
            else:
                if not silent:
                    print("nothing to load")
                return
        else:
            tarpath = Path(tarpath)
            if not silent:
                print(f"loading given backup: {tarpath}, {tarpath.stat().st_size / 1000 / 1000} MB")

        self.context['backup'] = tarpath
        info = extract_dumpinfo(str(tarpath))
        self.context['dump_version'] = info['dump_version']
        self.context['system_migration_files'] = info['system_migration_files']
        self.context['size_bytes'] = Path(tarpath).stat().st_size

        if not silent:
            print(f"created at: {info['created_at']}")
            print(f"[dump-version (for)]  \t {self.context['dump_version']}")
            print(f"[system-version (now)]\t {self.context['system_version']}")
            print(f"[dump-migrations]     \t {self.context['system_migration_files']}")
            print(
                f"[system-migrations]   \t {self.system_migration_files} (found) / {self.context['system_migrations_migrated']} (applied)\n")

        if not loadmigrations:
            if self.migration_not_found:
                self.stdout.write(self.style.ERROR("there are migration files missing on your system:"))
                self.stdout.write(self.style.ERROR(self.migration_not_found))
                members = []
                for migration in str(self.migration_not_found).split("\n"):
                    member = check_member(tarpath, f"_migration_backup/{migration}")
                    if member:
                        members.append(migration)
                if members:
                    if not silent:
                        print(f"this backup also contains:")
                    for each in members:
                        print("\t" + each)
                    if not silent:
                        print("\n use parameter --loadmigrations to restore them")
                text = f"Migration {self.migration_not_found} was not found;"
                if members:
                    text += f"however this backup contains {members}, you can restore them via --loadmigrations"
                raise MigrationNotFound(text)

        if not noinput:
            result = create_input()
            if not result:
                if not silent:
                    print("abort")
                return

        if not tarpath.is_file():
            raise Exception(f"file {tarpath} does not exist")

        if loadmigrations:
            extract_tar(str(tarpath), "_migration_backup", strip=1)

        extract_tar(tarpath, member_path=BackupUtilsConfig.JSON_FILENAME)

        if flush:
            flush_db()

        if not skiptest:
            verbosity = 3
            if silent:
                verbosity = 0
            print()
            logger.debug(f"running database restore test ...\n")
            suite = unittest.defaultTestLoader.loadTestsFromTestCase(loaddata.TestMigration)
            result = unittest.TextTestRunner(verbosity=verbosity).run(suite)

            if result.errors:
                logger.error(f"failed unittest:\n{result.errors}")
                raise UnittestFailed(message=f"unittest failed", output=str(result.errors[0]), **self.context)

        load_database_dump(self.json_path, **self.context)

        if deletedirs:
            logger.debug(f"trying to delete {settings.BACKUP_DIRS}...")
            for dir in settings.BACKUP_DIRS:
                delete_dir(dir, **self.context)

        # restore backup_dirs
        for each in settings.BACKUP_DIRS:
            extract_tar(tarpath, dir=each)

        logger.debug(f"removing {self.json_path}")
        os.remove(self.json_path)

        if not self.json_path.exists():
            self.stdout.write(self.style.SUCCESS(f"successfully restored backup: {tarpath}"))
            models.BackupLog.objects.create(message="loaded backup",
                                            module=module,
                                            success=True,
                                            size_bytes=self.context['size_bytes'],
                                            backup=self.context['backup'],
                                            params=self.context['params'])
