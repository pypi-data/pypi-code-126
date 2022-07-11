# Standard library imports.
import datetime

# pytz package imports.
from pytz import UTC

# qrazyv package imports.
import qrazyv

# Local package imports.
from tsofa.views._base import Base


class View(Base):

    @classmethod
    def export(cls, url, sdate, edate, sids, strip_rev = False):

        # Define a dictionary that will contain a list of documents
        # in a format that the CouchDB "bulk_docs" endpoint would
        # accept.
        docs = {'docs': []}

        # Define the inner callback to be sent to the qrazyv queries
        # function.
        def _inner(query, query_num, row, row_num):

            doc = row['doc']

            if strip_rev == True:
                del doc['_rev']

            docs['docs'].append(doc)

            return None

        # Generate multiple queries for batch requesting of the lister
        # data.
        queries = []

        for sid in sids:
            queries.append({
                'startkey': [sid] + cls.dkg(sdate),
                'endkey': [sid] + cls.dkg(edate) + [u'fff0'],
                'include_docs': 'true',
                'reduce': 'false'})

        # Perform the request to the database.  The _inner function
        # will populate the return value.
        cls.queries(url, queries, callback = _inner)

        return docs

    @classmethod
    def latest(cls, url, sdate, edate, sids, **kwargs):

        data = {}

        # If there is a string template provided, then date output
        # will be output as a string with the given format.
        tmpl = kwargs.get('tmpl')

        # Define the inner callback to be sent to the qrazyv queries
        # function.
        def _inner(query, query_num, row, row_num):

            sid = row['key'][0]
            doc = row['doc']

            if sid not in data:
                data[sid] = {}

            data[sid] = [cls.dkp(row['key'], edate.tzinfo, tmpl = tmpl), doc]

            return None

        # Generate multiple queries for batch requesting of the latest
        # data.
        queries = []

        for sid in sids:
            queries.append({
                'startkey': [sid] + cls.dkg(edate) + [u'fff0'],
                'endkey': [sid] + cls.dkg(sdate),
                'include_docs': 'true',
                'reduce': 'false',
                'descending': 'true',
                'limit': 1})

        # Perform the request to the database.  The _inner function
        # will populate the return value.
        cls.queries(url, queries, callback = kwargs.get('callback', _inner))

        return data

    @classmethod
    def lister(cls, url, sdate, edate, sids, **kwargs):

        _data = {}

        # If there is a string template provided, then date output
        # will be output as a string with the given format.
        tmpl = kwargs.get('tmpl')

        # Define the callback function to handle row processing for
        # this method.
        def _inner(query, query_num, row, row_num):

            # Get the station ID from the key.
            sid = row['key'][0]

            # Get the document from the row.
            doc = row['doc']

            # Generate a datetime object from the key.
            date = cls.dkp(row['key'], edate.tzinfo, tmpl = tmpl)

            if type(date) == type(''):
                dstr = date

            else:
                dstr = date.strftime('%Y-%m-%dT%H:%M:%S%z')

            if sid not in _data:
                _data[sid] = {}

            if dstr not in _data[sid]:
                _data[sid][dstr] = [date, doc]

            return None

        # Generate multiple queries for batch requesting of the lister
        # data.
        queries = []

        for sid in sids:
            queries.append({
                'startkey': [sid] + cls.dkg(sdate),
                'endkey': [sid] + cls.dkg(edate) + [u'fff0'],
                'include_docs': 'true',
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
    def pors(cls, url, tzinfo, sids, **kwargs):

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
            date = cls.dkp(row['key'], tzinfo, tmpl = tmpl)

            if sid not in data:
                data[sid] = [None, None]

            if 'descending' in query:
                data[sid][1] = date

            else:
                data[sid][0] = date

            return None

        # Generate multiple queries for batch requesting of the pors
        # data.
        queries = []

        for sid in sids:

            # Define two queries per series ID, one for the first
            # instance of data, the second for the last.
            q1 = {
                'startkey': [sid],
                'endkey': [sid, u'fff0'],
                'reduce': 'false',
                'limit': 1}
            q2 = {
                'startkey': [sid, u'fff0'],
                'endkey': [sid],
                'reduce': 'false',
                'descending': 'true',
                'limit': 1}
            queries.extend([q1, q2])

        # Perform the request to the database.  The _inner function
        # will populate the return value.
        cls.queries(url, queries, callback = kwargs.get('callback', _inner))

        return data
