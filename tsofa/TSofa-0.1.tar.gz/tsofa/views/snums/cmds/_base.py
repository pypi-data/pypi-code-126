# Local package imports
from tsofa.views._base_cmd import Command as Base


class Command(Base):

    module = None
    tmpl = '%Y-%m-%dT%H:%M:%S%z'

    def add_subparser_arguments(self, sp):

        super(Command, self).add_subparser_arguments(sp)

        summary = sp.add_parser('summary')
        summary.add_argument(
            'sdate',
            type = self.arg_date,
            help = 'Retrieve data from this date')
        summary.add_argument(
            'edate',
            type = self.arg_date,
            help = 'Retrieve data up to this date')
        summary.add_argument(
            '--sids',
            nargs = '*',
            help = 'Retrieve data only for these stations')
        summary.add_argument(
            '--elems',
            nargs = '*',
            help = 'Retrieve data for these data elements')

        sl = sp.add_parser('slister')
        sl.add_argument(
            'sdate',
            type = self.arg_date,
            help = 'Retrieve data from this date')
        sl.add_argument(
            'edate',
            type = self.arg_date,
            help = 'Retrieve data up to this date')
        sl.add_argument(
            'interval',
            help = 'Specify the code that determines the interval.')
        sl.add_argument(
            '--sids',
            nargs = '*',
            help = 'Retrieve data only for these stations')
        sl.add_argument(
            '--elems',
            nargs = '*',
            help = 'Retrieve data for these data elements')

        return None

    def handle(self, *args, **kwargs):

        output = super(Command, self).handle(*args, **kwargs)

        if kwargs['cmd'] == 'summary':
            output = self.module.summary(
                kwargs['db'],
                kwargs['sdate'],
                kwargs['edate'],
                kwargs['sids'],
                kwargs['elems'])
        if kwargs['cmd'] == 'slister':
            output = self.module.slister(
                kwargs['db'],
                kwargs['sdate'],
                kwargs['edate'],
                kwargs['sids'],
                kwargs['elems'],
                interval = kwargs['interval'],
                tmpl = self.tmpl)

        return output
