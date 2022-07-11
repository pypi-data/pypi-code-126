# Standard library imports.
import datetime

# pytz package imports.
from pytz import UTC

# qrazyv package imports.
import qrazyv


class Base:

    # View to query for series data element values.
    view = '/_design/_/_view/_/'

    # Define a string template for creating a date key from a
    # datetime.datetime object.  Date keys are used for database
    # queries.
    dk_tmpl = '["%Y","%m","%d","%H","%M","%S"]'

    @classmethod
    def _export(cls):

        methods = {}

        for attr in dir(cls):

            if not attr.startswith('_'):

                _obj = getattr(cls, attr, None)

                if callable(_obj):
                    methods[attr] = _obj

        return methods

    @classmethod
    def _get_view(cls, url):

        view = ''

        # If the url parameter is a dictionary, assume it contains the
        # URL to a CouchDB database (with no authentication
        # information) and a session cookie value.  If it is a string
        # type, then assume that it is a database URL (with basic
        # authentication information) and add the class view value to
        # the end.
        if type(url) == type({}):
            view = {
                'view': url.get('url', '') + cls.view,
                'AuthSession': url.get('AuthSession', 'null')}

        elif type(url) == type(''):
            view = url + cls.view

        return view

    @classmethod
    def dkg(cls, date):
        """Generates a list of datetime object components.

        The generated list may be used to perform a database request
        for data over some date range.

        """
        # Adjust the date to UTC time.
        date = date.astimezone(UTC)

        # Format and evaluate the UTC date as list, then return.
        return eval(date.strftime(cls.dk_tmpl))

    @classmethod
    def dkp(cls, key, tzinfo, tmpl = None):
        """Parses a datetime object from a database row key.

        """
        # Determine the starting index of the date key based on the
        # dk_tmpl class variable.
        idxs = len(cls.dk_tmpl.split(',')) * -1

        # Construct a string of date components from the date key.
        dc = ''

        for i in range(idxs, 0):
            dc += str(int(key[i])) + ','

        # Now, try to create the actual datetime or date object.
        try:

            date = eval('datetime.datetime({})'.format(dc))
            date = UTC.localize(date).astimezone(tzinfo)

            if type(tmpl) == type(''):
                date = date.strftime(tmpl)

        except:
            date = None

        return date

    @classmethod
    def queries(cls, url, queries, callback = None):
        """Perform multi-query database request.

        """
        # Perform the request to the database.  The _ callback
        # parameter function may populate the return value.
        output = qrazyv.queries(
            cls._get_view(url), queries, callback = callback)

        return output

    @classmethod
    def sids(cls, url, **kwargs):
        """Returns a list of data series indicies from the database.

        Series ID indices may be thought of as a unique identifier of
        a single sheet (table) in a spreadsheet.

        The Series ID indices are returned in a list and each item of
        the list is guaranteed to be unique, due to the behavior of
        the database.

        """
        sids = []

        # Define the callback function to handle row processing for
        # this method.
        def _inner(query, query_num, row, row_num):
            sids.append(row['key'][0])

        # Perform the request to the database.  The _inner function
        # will populate the return value.
        queries = [{'group_level': 1}]

        # Perform the data request.
        cls.queries(url, queries, callback = kwargs.get('callback', _inner))

        return sids


class View(Base):

    @classmethod
    def elems(cls, url, **kwargs):
        """Get a dictionary of data element indices from the database.

        Data element indices can be thought of as the headers of the
        columns in a singular sheet of a spreadsheet.

        These indices are returned as list objects mapped to the unique
        series ID indices.  Due to the behavior of the database, the
        data element indices are guaranteed to be unique on a per
        series ID basis.

        As an example, suppose we have two series ID indices "xyz" and
        "tuv". Data element indices in the database may include "a",
        "b", and "c".  The dictionary may look like this:

        {
            "xyz": ["a", "c"],
            "tuv": ["b", "c"]
        }

        This means that for the series index "xyz", data is stored in
        the database for only element indices "a" and "c".  Further,
        only values for data element indices "b" anc "c" are stored in
        the database using the "tuv" series index.

        """
        data = {}

        # Define the inner callback to be sent to the qrazyv queries
        # function.
        def _inner(query, query_num, row, row_num):

            sid = row['key'][0]
            value = row['key'][1]

            if sid not in data:
                data[sid] = []

            if value not in data[sid]:
                data[sid].append(value)

            return None

        # Define the queries.  In this case, just one query.
        queries = [{'group_level': 2}]

        # Perform the request to the database.  The _inner function
        # will populate the return value.
        cls.queries(url, queries, callback = kwargs.get('callback', _inner))

        return data

    @classmethod
    def latest(cls, url, sdate, edate, sids, elems, **kwargs):
        """Get the latest values from the database.

        Given a date range, a list of series ID indices, and data
        element indices, return the latest values in the database for
        those parameters.  If unsure of how long ago the latest values
        were recorded, set the start date to date and time far into the
        past.

        Data is returned as dictionaries mapped to the unique series ID
        indices.  Within these dictionaries, two item lists are mapped
        to data element index keys.  The first item in these lists are
        the date of the latest occurance of data for the element, and
        the second item is the value of the occurance.

        As an example, suppose we have the series ID indices "xyz" and
        "tuv".  Data for element indices "a" and "c" have been stored
        in the database using the "xyz" series index.  For the "tuv"
        index, data is stored for the "b" and "c" element indices.

        {
            'xyz':
                {
                    'a': ['2022-06-12', 1],
                    'c': ['2022-06-16', 3]
                },
            'tuv':
                {
                    'b': ['2022-06-16', 'abc'],
                    'c': ['2022-06-12', 4]
                }
        }

        Although data element indices exist within separate series, the
        values are unique to those series.

        If a series ID or a data element ID index are given in the
        input parameters, but they do not exist in the database, then
        those indices will not appear as keys within the return value.

        """
        data = {}

        # If there is a string template provided, then date output
        # will be output as a string with the given format.
        tmpl = kwargs.get('tmpl')

        # Define the inner callback to be sent to the qrazyv queries
        # function.
        def _inner(query, query_num, row, row_num):

            sid = row['key'][0]
            elem = row['key'][1]

            if sid not in data:
                data[sid] = {}

            data[sid][elem] = [
                cls.dkp(row['key'], sdate.tzinfo, tmpl = tmpl), row['value']]

            return None

        # Generate multiple queries for batch requesting of the latest
        # data.
        queries = []

        for sid in sids:
            for elem in elems:
                queries.append({
                    'startkey': [sid, elem] + cls.dkg(edate) + [u'fff0'],
                    'endkey': [sid, elem] + cls.dkg(sdate),
                    'reduce': 'false',
                    'descending': 'true',
                    'limit': 1})

        # Perform the request to the database.  The _inner function
        # will populate the return value.
        cls.queries(url, queries, callback = kwargs.get('callback', _inner))

        return data

    @classmethod
    def lister(cls, url, sdate, edate, sids, elems, **kwargs):
        """Request listings of data by series ID and ordered by date.

        Data is returned as ordered lists that are mapped to the unique
        series ID indices.  Each item in the ordered lists is a two
        item list, where the first item is the date, and the second
        item is a dictionary with values mapped to the data element
        indices.  The parent list is ordered by the date in the first
        item of all the sub-lists.

        {
            'xyz':
                [
                    ['2022-06-01', {'a': 1, 'c': 2}],
                    ['2022-06-02', {'c': 9}],
                    ['2022-06-03', {'a': 2}],
                    ['2022-06-05', {'a': 4, 'c': 0}],
                    ...
                    ['2022-06-12', {'a': 1}]
                    ['2022-06-16', {'c': 3}]
                ]
        }

        Notice that the lists have missing days of data.  This method
        does not fill in those missing days.  If data doesn't exist
        for the data element indices and the series index, not even an
        empty data structure will be added.

        """
        _data = {}

        # If there is a string template provided, then date output
        # will be output as a string with the given format.
        tmpl = kwargs.get('tmpl')

        # Define the callback function to handle row processing for
        # this method.
        def _inner(query, query_num, row, row_num):

            # Get the station ID from the key.
            sid = row['key'][0]

            # Get the data element from the key.
            elem = row['key'][1]

            # Get the value from the row.
            value = row['value']

            # Generate a datetime object from the key.
            date = cls.dkp(row['key'], sdate.tzinfo, tmpl = tmpl)

            if type(date) == type(''):
                dstr = date

            else:
                dstr = date.strftime('%Y-%m-%dT%H:%M:%S%z')

            if sid not in _data:
                _data[sid] = {}

            if dstr not in _data[sid]:
                _data[sid][dstr] = [date, {}]

            _data[sid][dstr][1][elem] = value

            return None

        # Generate multiple queries for batch requesting of the lister
        # data.
        queries = []

        for sid in sids:
            for elem in elems:
                queries.append({
                    'startkey': [sid, elem] + cls.dkg(sdate),
                    'endkey': [sid, elem] + cls.dkg(edate) + [u'fff0'],
                    'reduce': 'false'})

        # Perform the request to the database.  The _inner function
        # will populate the return value.
        cls.queries(url, queries, callback = kwargs.get('callback', _inner))

        # The final data location.
        data = {}

        # A lambda function for use in sorting of the rows of data.
        f = lambda x: x[0]

        for sid in _data.keys():
            data[sid] = sorted(list(_data[sid].values()), key = f)

        return data

    @classmethod
    def pors(cls, url, tzinfo, sids, elems, **kwargs):
        """Retrieve the first and latest occurrances of data.

        Given lists of series ID indices and data element indices, get
        the first and latest occurances of values for those indices.
        Data is returned as dictionaries with two item lists mapped to
        the data element indices.  The first item in the list is the
        date of first occurance, and the second item is the latest date
        of occurance.  The data element dictionaries are then further
        mapped to the unique series ID indices.

        {
            'tuv':
                {
                    'b': ['2022-05-01', '2022-06-16'],
                    'c': ['2022-06-05', '2022-06-12']
                }
        }

        """
        data = {}

        # If there is a string template provided, then date output
        # will be output as a string with the given format.
        tmpl = kwargs.get('tmpl')

        # Define the callback function to handle row processing for
        # this method.
        def _inner(query, query_num, row, row_num):

            # Get the series ID, the data element ID and the date from
            # the row key.
            sid = row['key'][0]
            elem = row['key'][1]
            date = cls.dkp(row['key'], tzinfo, tmpl = tmpl)

            if sid not in data:
                data[sid] = {}

            if elem not in data[sid]:
                data[sid][elem] = [None, None]

            if 'descending' in query:
                data[sid][elem][1] = date

            else:
                data[sid][elem][0] = date

            return None

        # Generate multiple queries for batch requesting of the pors
        # data.
        queries = []

        for sid in sids:

            for elem in elems:

                # Define two queries per series ID, one for the first
                # instance of data, the second for the last.
                q1 = {
                    'startkey': [sid, elem],
                    'endkey': [sid, elem, u'fff0'],
                    'reduce': 'false',
                    'limit': 1}
                q2 = {
                    'startkey': [sid, elem, u'fff0'],
                    'endkey': [sid, elem],
                    'reduce': 'false',
                    'descending': 'true',
                    'limit': 1}
                queries.extend([q1, q2])

        # Perform the request to the database.  The _inner function
        # will populate the return value.
        cls.queries(url, queries, callback = kwargs.get('callback', _inner))

        return data
