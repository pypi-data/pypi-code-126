# -*- coding: utf-8 -*-
import sys
import os
import re
import shutil
import argparse
import logging
from datetime import datetime

CONF_FILENAME = 'dir_clean.conf'

RETURN_CODE_CONF_FILE_NOT_FOUND = 1

log = logging.getLogger(__package__)


def parse_cmdline():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--keep-days', type=int, default=7, help='days to keep (default: 7)')
    parser.add_argument('-c', '--conf-file', help='configuration filename (default: %s)' % CONF_FILENAME)
    parser.add_argument('--dry-run', action='store_true')

    opts = parser.parse_args(sys.argv[1:])
    return opts


def remove(file_or_path):
    if os.path.isfile(file_or_path):
        try:
            os.remove(file_or_path)
        except:
            pass
    else:
        shutil.rmtree(file_or_path, ignore_errors=True)

    if os.path.exists(file_or_path):
        log.warning('%s remove failed!' % file_or_path)


def clean(conf_tuple, dry_run=False):
    now = datetime.now()

    path, regex, keep_days = conf_tuple
    log.info('---- path: %s ---- regex: %s ---- keep-days: %d ----' % (path, regex, keep_days))

    for rela_path in os.listdir(path):

        modify_date = None
        if regex:
            m = re.match(regex, rela_path)
            if not m:
                continue

            try:
                y, m, d = map(int, [m.group(a) for a in 'ymd'])
                modify_date = datetime(y, m, d)
            except Exception as e:
                pass

        abs_filepath = os.path.join(path, rela_path)

        if not modify_date:
            mtime = os.stat(abs_filepath).st_mtime
            modify_date = datetime.fromtimestamp(mtime)

        days = (now - modify_date).days
        if days <= keep_days:
            continue

        log.info('removing %s  (%s => %d > %d days)' % (abs_filepath, modify_date.date().isoformat(), days, keep_days))
        if not dry_run:
            remove(abs_filepath)


def main():
    opts = parse_cmdline()

    conf_file = opts.conf_file or CONF_FILENAME
    if not os.path.isfile(conf_file):
        log.error('%s not exists!' % conf_file)
        return RETURN_CODE_CONF_FILE_NOT_FOUND

    with open(CONF_FILENAME) as f:
        lines = list(filter(lambda x: x and not x.startswith('#'), map(str.strip, f.readlines())))

    conf_tuples = []
    for line in lines:
        regex = None
        days = opts.keep_days

        params = line.split(',')
        if len(params) == 1:
            path = params[0]
        elif len(params) == 2:
            path, regex = params
        elif len(params) == 3:
            path, regex, days = params
            days = int(days)
        else:
            raise RuntimeError('config line should be <path>,[regex],[keep-days]')

        conf_tuples.append((path, regex, days))

    for conf_tuple in conf_tuples:
        clean(conf_tuple, opts.dry_run)

    return 0


if __name__ == '__main__':
    ret = main()
    sys.exit(ret)
