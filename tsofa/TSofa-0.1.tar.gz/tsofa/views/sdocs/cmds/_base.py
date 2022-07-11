# Standard library imports.
import json
from argparse import ArgumentTypeError as Err
from datetime import datetime

# pytz package imports.
import pytz

# Two-Percent package imports.
from twopct.base import Command as Base

# Local package imports.
from tsofa.views._base_cmd import TMP_DT


class Command(Base):

    def add_arguments(self, parser):

        parser.add_argument(
            '--tz',
            type = self.arg_tz,
            default = 'US/Mountain',
            help = 'Specify timezone for date input and data output')
        parser.add_argument(
            'db',
            type = str,
            help = 'URL to a CouchDB database')

        self.add_subparser_arguments(parser.add_subparsers(dest = 'cmd'))

        return None

    def add_subparser_arguments(self, sp):

        export = sp.add_parser('export')
        export.add_argument(
            'sdate',
            type = self.arg_date,
            help = 'Retrieve documents from this date')
        export.add_argument(
            'edate',
            type = self.arg_date,
            help = 'Retrieve documents up to this date')
        export.add_argument(
            '--sids',
            nargs = '*',
            help = 'Retrieve document only for these series')
        export.add_argument(
            '--strip_rev',
            action = 'store_true',
            help = 'Strip the revision attribute from the documents')

        latest = sp.add_parser('latest')
        latest.add_argument(
            'sdate',
            type = self.arg_date,
            help = 'Retrieve data from this date')
        latest.add_argument(
            'edate',
            type = self.arg_date,
            help = 'Retrieve data up to this date')
        latest.add_argument(
            '--sids',
            nargs = '*',
            help = 'Retrieve data only for these series')

        lister = sp.add_parser('lister')
        lister.add_argument(
            'sdate',
            type = self.arg_date,
            help = 'Retrieve data from this date')
        lister.add_argument(
            'edate',
            type = self.arg_date,
            help = 'Retrieve data up to this date')
        lister.add_argument(
            '--sids',
            nargs = '*',
            help = 'Retrieve data only for these series')

        pors = sp.add_parser('pors')
        pors.add_argument(
            '--sids',
            nargs = '*',
            help = 'Retrieve data only for these series')

        sids = sp.add_parser('sids')

        return None

    def arg_date(self, str_value):

        date = None
        count = 0

        while count < len(TMP_DT):

            try:
                date = datetime.strptime(str_value, TMP_DT[count])

            except:
                date = None

            if date != None:
                count = len(TMP_DT)

            count += 1

        if date is None:
            raise Err('{} is not a valid date'.format(str_value))

        return date

    def arg_tz(self, str_value):

        try:
            tz = pytz.timezone(str_value)

        except:
            raise Err('{} is not a valid time zone'.format(str_value))

        return str_value

    def clean(self, **kwargs):

        cleaned = {}

        if 'sdate' in kwargs:
            cleaned['sdate'] = self.clean_date(kwargs['sdate'], kwargs['tz'])

        if 'edate' in kwargs:
            cleaned['edate'] = self.clean_date(kwargs['edate'], kwargs['tz'])

        if 'sids' in kwargs:
            if kwargs['sids'] == None:
                cleaned['sids'] = []

        return cleaned

    def clean_date(self, date, tz):

        if 'datetime.datetime' in str(type(date)):

            try:
                output = pytz.timezone(tz).localize(date)

            except:
                output = pytz.UTC.localize(date)

        else:
            output = date

        return output

    def dumps(self, value, **kwargs):
        return json.dumps(value)

    def handle(self, *args, **kwargs):

        output = None

        if kwargs['cmd'] == 'export':
            output = self.module.export(
                kwargs['db'],
                kwargs['sdate'],
                kwargs['edate'],
                kwargs['sids'],
                strip_rev = kwargs.get('strip_rev'))

        elif kwargs['cmd'] == 'latest':
            output = self.module.latest(
                kwargs['db'],
                kwargs['sdate'],
                kwargs['edate'],
                kwargs['sids'],
                tmpl = self.tmpl)

        elif kwargs['cmd'] == 'lister':
            output = self.module.lister(
                kwargs['db'],
                kwargs['sdate'],
                kwargs['edate'],
                kwargs['sids'],
                tmpl = self.tmpl)

        elif kwargs['cmd'] == 'pors':
            output = self.module.pors(
                kwargs['db'],
                pytz.timezone(kwargs['tz']),
                kwargs['sids'],
                tmpl = self.tmpl)

        elif kwargs['cmd'] == 'sids':
            output = self.module.sids(kwargs['db'])

        return output
