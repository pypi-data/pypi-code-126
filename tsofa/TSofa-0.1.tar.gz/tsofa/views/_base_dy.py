# Standard library imports.
import datetime


class MixInDy:

    # Define a string template for creating date keys with daily
    # resolution.
    dk_tmpl = '["%Y","%m","%d"]'

    @classmethod
    def dkg(cls, date):
        """Generates a list of date object components.

        The generated list may be used to perform a database request
        for data over some date range.

        """
        # Get the date object from the given datetime object.
        date = date.date()

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
            date = tzinfo.localize(date)

            if type(tmpl) == type(''):
                date = date.strftime(tmpl)

        except:
            date = None

        return date
