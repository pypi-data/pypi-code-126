# -*- coding:utf-8 -*-

import argparse
import json
import os
import shutil
import sys

from com.dvsnier.android import DEBUGGER, VERSIONS
from com.dvsnier.config.journal.compat_logging import logging
from os import fdopen
from tempfile import mkstemp


def execute(args=None):
    '''
        the execute command

        it is that reference link:

            1. https://docs.python.org/zh-cn/3/library/argparse.html
            2. https://docs.python.org/zh-cn/2/library/argparse.html
    '''
    if args is None:
        args = sys.argv[1:]
    logging.set_kw_output_dir_name(os.path.join(
        os.getcwd(), 'build', 'dvs-android')).set_kw_file_name('log').set_kw_level(
            logging.DEBUG).set_logging_name('dvs-android').set_logging_formatter(format_style=logging.DEBUG).build(
                console_only=False)
    parser = argparse.ArgumentParser(
        prog='dvs-android',
        description="""
    this is a dvs android execution program.
        """,
        epilog='the copyright belongs to DovSnier that reserve the right of final interpretation.\n',
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-V', '--version', action='version', version=VERSIONS, help='the show version and exit.')
    parser.add_argument(
        'build_file',
        action='store',
        nargs='?',
        default=os.getcwd(),
        type=str,
        metavar='build-file',
        # dest='build_file',
        help='the current app project build file absolute path.')
    parser.add_argument(
        '-id',
        '--application-id',
        action='store',
        nargs='?',
        type=str,
        metavar='application-id',
        # dest='application_id',
        help='the android application id property.')
    parser.add_argument(
        '-vn',
        '--version-name',
        action='store',
        nargs='?',
        type=str,
        metavar='version-name',
        # dest='version_name',
        help='the android version name property.')
    parser.add_argument(
        '-vc',
        '--version-code',
        action='store',
        nargs='?',
        default=1,
        type=int,
        metavar='version-code',
        # dest='version_code',
        help='the android version code property.')
    args = parser.parse_args(args)
    run(args)


def run(args):
    ''' the run script command '''
    if args:
        if args.build_file and os.path.exists(args.build_file):
            PREFIX = 'dvs-android-build-gradle-'
            SUFFIX = '.tmp'
            BUILD_DOT_GRADLE = 'build.gradle'
            fd, abspath = mkstemp(prefix=PREFIX, suffix=SUFFIX)
            with fdopen(fd, 'w') as build_file_new:
                with open(args.build_file, 'r') as build_file:
                    lines_content = build_file.readlines()
                    for line_content in lines_content:
                        if line_content and len(line_content.strip()) > 0:
                            split_value = line_content.strip().split(' ')
                            if split_value and len(split_value) >= 2:
                                if args.application_id and type(
                                        args.application_id
                                ) == str and 'applicationId' == split_value[0]:  # applicationId
                                    build_file_new.write(
                                        '        ' + split_value[0] + ' ' + '\"' +
                                        split_value[1].replace(split_value[1], args.application_id.strip()) + '\"' +
                                        '\n')
                                    logging.debug('the {} attribute is currently modified, and the value is {}.'.format(
                                        'applicationId', args.application_id.strip()) + ' The execution is passed.')
                                elif args.version_name and type(
                                        args.version_name) == str and 'versionName' == split_value[0]:  # versionCode
                                    build_file_new.write(
                                        '        ' + split_value[0] + ' ' + '\"' +
                                        split_value[1].replace(split_value[1], args.version_name.strip()) + '\"' + '\n')
                                    logging.debug('the {} attribute is currently modified, and the value is {}.'.format(
                                        'versionName', args.version_name.strip()) + ' The execution is passed.')
                                elif args.version_code and type(
                                        args.version_code) == int and 'versionCode' == split_value[0]:  # versionCode
                                    build_file_new.write(
                                        '        ' + split_value[0] + ' ' +
                                        split_value[1].replace(split_value[1], str(args.version_code)) + '\n')
                                    logging.debug('the {} attribute is currently modified, and the value is {}.'.format(
                                        'versionCode', str(args.version_code)) + ' The execution is passed.')
                                else:
                                    # logging.error('The current parameter({}) is illegal, so the parsing exits.',
                                    #   args.version_name)
                                    # logging.error('The current parameter({}) is illegal, so the parsing exits.',
                                    #   args.version_code)
                                    build_file_new.write(line_content)
                            else:
                                build_file_new.write(line_content)
                        else:
                            build_file_new.write(line_content)
            if os.path.exists(os.path.join(os.path.dirname(abspath), BUILD_DOT_GRADLE)):
                os.remove(os.path.join(os.path.dirname(abspath), BUILD_DOT_GRADLE))
                # os.rename(os.path.join(os.path.dirname(abspath), os.path.basename(abspath)),
                #   os.path.join(os.path.dirname(abspath), BUILD_DOT_GRADLE))
            if os.path.exists(os.path.join(os.path.dirname(abspath), os.path.basename(abspath))):
                os.remove(args.build_file)
                shutil.copyfile(os.path.join(os.path.dirname(abspath), os.path.basename(abspath)),
                                os.path.join(os.path.dirname(args.build_file), BUILD_DOT_GRADLE))
                os.remove(os.path.join(os.path.dirname(abspath), os.path.basename(abspath)))
                logging.info('the current task execution completed.')
        else:
            if args.build_file:
                logging.error(
                    'the current path({}) cannot find build.gradle configuration file, parse and return.'.format(
                        args.build_file))
            else:
                logging.error(
                    'the current path(args::build-file) cannot find build.gradle configuration file, parse and return.')
    if DEBUGGER:
        # print('vars(args): {}'.format(vars(args)))
        logging.warning('the current config(args): {}'.format(json.dumps(vars(args), indent=4)))


if __name__ == "__main__":
    '''the main function entry'''
    execute()
