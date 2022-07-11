# Standard library imports.
import datetime
from math import sqrt

# QrazyV package imports.
import qrazyv

# Local package imports.
from tsofa.views._base import View as Base


class View(Base):

    # Define the minimum interval between reports in the database.
    delta = datetime.timedelta(seconds = 1)

    # Define the allowed intervals used to create a summary lister.
    intervals = ('days', 'hours', 'minutes', 'seconds')

    @classmethod
    def _get_delta(cls, interval):

        td = None

        try:

            ival = interval[2:-1]

            for i in cls.intervals:

                if td == None:

                    if i in ival:

                        num = ival.replace(i, '')
                        td = eval('datetime.timedelta(' + i + '=' + num + ')')

            if td <= cls.delta:
                td = None

        except:
            td = None

        return td

    @classmethod
    def avgstd(cls, stats):
        """Generates average and standard deviation statistics.

        Given a dictionary containing statistics values returned from
        the built-in "_stats" reduction function in the CouchDB
        database, calculate the average and standard deviation.  The
        "sumsqr" and "count" attributes are renamed in the process to
        "ssq" and "num", respectively.

        """
        ns = {}

        for s in stats:

            if s == 'sumsqr':
                ns['ssq'] = stats['sumsqr']

            elif s == 'count':
                ns['num'] = stats['count']

            else:
                ns[s] = stats[s]

        if ns.get('num', 0) > 0:
            ns['avg'] = ns['sum'] / ns['num']

        if ns.get('num', 0) > 1:

            _sum = ns['sum']
            _ssq = ns['ssq']
            _num = ns['num']

            try:
                ns['std'] = sqrt((_ssq - ((_sum * _sum) / _num)) / (_num - 1))

            except:
                ns['std'] = None

        return ns

    @classmethod
    def slister(cls, url, sdate, edate, sids, elems, interval, **kwargs):
        """Provides a listing of sumaaries of data over date intervals.

        """
        _data = {}

        # Get the timedelta object that defines the summary interval.
        #interval = kwargs.get('interval')
        delta = cls._get_delta(interval)

        # If the interval starts with a "-", that means that for each
        # date in the interval, the summarized data will be from the
        # previous date to the current date.  So, use the endkey to
        # report the summarized data in the lister.
        use_key = 'startkey'

        if interval.startswith('n') == True:
            use_key = 'endkey'

        # If there is a string template provided, then date output
        # will be output as a string with the given format.
        tmpl = kwargs.get('tmpl')

        # Define the callback to process the summaries.
        def _inner(query, query_num, row, row_num):

            # Get the station ID from the key.
            sid = query[use_key][0]

            # Get the data element from the key.
            elem = query[use_key][1]

            # Generate a date object from the key.
            date = cls.dkp(query[use_key], sdate.tzinfo, tmpl = tmpl)

            if type(date) == type(''):
                dstr = date

            else:
                dstr = date.strftime('%Y-%m-%dT%H:%M:%S%z')

            # Get the value from the row.
            value = row['value']

            if sid not in _data:
                _data[sid] = {}

            if dstr not in _data[sid]:
                _data[sid][dstr] = [date, {}]

            _data[sid][dstr][1][elem] = cls.avgstd(value)

            return None

        # Copy the given datatime objects to build queries.
        sd = cls.dkp(cls.dkg(sdate), sdate.tzinfo)
        ed = cls.dkp(cls.dkg(edate), edate.tzinfo)

        # Use this template to compare the start date to the end date
        # as the query generation iteration is performed.
        _tmpl = '%Y-%m-%dT%H:%M:%S%z'

        # Generate the queries for requesting summary interval data.
        queries = []

        if delta is not None:

            while sd.strftime(_tmpl) <= ed.strftime(_tmpl):

                # Create the start and end dates for the intervals
                # that will be summarized.
                if interval.startswith('p'):

                    _sd = sd
                    _ed = sd + delta

                else:

                    _sd = sd - delta
                    _ed = sd

                if interval[1] == 'X':
                    _sd = _sd + cls.delta

                if interval[-1] == 'X':
                    _ed = _ed - cls.delta

                # Loop over the series ID indices and the data element
                # indices, creating the queries for each.
                for sid in sids:
                    for elem in elems:
                        queries.append({
                            'startkey': [sid, elem] + cls.dkg(_sd),
                            'endkey': [sid, elem] + cls.dkg(_ed)})

                sd += delta

        # Perform the request to the database.  The _inner function
        # will populate the return value.
        cls.queries(url, queries, callback = kwargs.get('callback', _inner))

        # The final data location.
        data = {}

        # Sort the data.
        for sid in _data.keys():
            data[sid] = sorted(
                list(_data[sid].values()), key = lambda x: x[0])

        return data

    @classmethod
    def ssummarize(cls, slister):
        """Generate statistics from a summary interval data lister.

        Given a series output of the "slister" method, generate the
        common statistics for the lister.  The max and min values of
        data elements will contain the date of occurrance.  This is a
        slower method of summarizing data, but comes with the benefit
        of providing the dates, as mentioned above, and of calculating
        on data that has already been retrieved.

        """
        data = {}

        for row in slister:

            date = row[0]

            for elem in row[1]:

                if elem not in data:
                    data[elem] = {}

                for stat in row[1][elem]:

                    value = row[1][elem][stat]

                    if stat not in data[elem]:
                        data[elem][stat] = {
                            'max': {'value': value, 'date': date},
                            'min': {'value': value, 'date': date},
                            'avg': None,
                            'sum': 0,
                            'num': 0}

                    if row[1][elem][stat] > data[elem][stat]['max']['value']:

                        data[elem][stat]['max']['value'] = row[1][elem][stat]
                        data[elem][stat]['max']['date'] = date

                    if row[1][elem][stat] < data[elem][stat]['min']['value']:

                        data[elem][stat]['min']['value'] = row[1][elem][stat]
                        data[elem][stat]['min']['date'] = date

                    data[elem][stat]['sum'] += row[1][elem][stat]
                    data[elem][stat]['num'] += 1

        for elem in data:
            for stat in data[elem]:
                if data[elem][stat]['num'] > 0:
                    data[elem][stat]['avg'] = \
                        data[elem][stat]['sum'] / data[elem][stat]['num']

        return data

    @classmethod
    def summarize(cls, lister):
        """Generate statistics from a data lister.

        Given a series output of the "lister" method, generate the
        common statistics for the lister.  The max an min values of
        data elements will contain the date of occurrance.  This is a
        slower method of summarizing data, but comes with the benefit
        of providing the dates, as mentioned above, and of calculating
        on data that has already been retrieved.

        """
        smry = {}

        for row in lister:

            for elem in row[1].keys():

                value = row[1][elem]
                date = row[0]

                if type(value) in (type(0), type(0.0)):

                    if elem not in smry.keys():
                        smry[elem] = {
                            'max': {'value': value, 'date': date},
                            'min': {'value': value, 'date': date},
                            'avg': None,
                            'sum': 0,
                            'num': 0}

                    if value > smry[elem]['max']['value']:

                        smry[elem]['max']['value'] = value
                        smry[elem]['max']['date'] = date

                    if value < smry[elem]['min']['value']:

                        smry[elem]['min']['value'] = value
                        smry[elem]['min']['date'] = date

                    smry[elem]['sum'] += value
                    smry[elem]['num'] += 1

        for elem in smry.keys():
            if smry[elem]['num'] > 0:
                smry[elem]['avg'] = smry[elem]['sum'] / smry[elem]['num']

        return smry

    @classmethod
    def summary(cls, url, sdate, edate, sids, elems, **kwargs):
        """Request a summary of data from the database.

        This method requests summary data using the built-in database
        "_stats" reduction functionality of the database view.  The
        summary data will be returned in a dictionary.  This is the
        faster way to summarize data, but the database reduce function
        can't report the dates of occurance for maximum and minimum
        statistics.

        """
        data = {}

        # Define the callback function to handle row processing for
        # this method.
        def _inner(query, query_num, row, row_num):

            sid = row['key'][0]
            elem = row['key'][1]
            value = cls.avgstd(row['value'])

            if sid not in data:
                data[sid] = {}

            data[sid][elem] = value

            return None

        # Create queries to get summary data from the database.
        queries = []

        for sid in sids:
            for elem in elems:
                queries.append({
                    'startkey': [sid, elem] + cls.dkg(sdate),
                    'endkey': [sid, elem] + cls.dkg(edate) + [u'fff0'],
                    'group_level': 2})

        # Perform the request to the database.  The _inner function
        # will populate the return value.
        cls.queries(url, queries, callback = kwargs.get('callback', _inner))

        return data
