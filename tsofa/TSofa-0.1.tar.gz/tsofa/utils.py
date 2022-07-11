# Standard library imports.
import random
from urllib import parse

# pytz package imports.
import pytz

# requests package imports.
import requests


def find_server(urls):
    """Given a list of CouchDB URL values, find an active server.

    """
    # Set this value to the first URL found where the hostname is found
    # to be an active CouchDB server.
    server = None

    # If the length of the urls is greater than zero, then continue
    # to attempt to find an active server.  Otherwise, do nothing
    # and return None.
    if len(urls) > 0:

        # Choose a random server from the given list.
        _temp = random.choice(urls)
        _alive = False

        # Parse the URL into its components.
        p = parse.urlsplit(_temp)

        # Split the "netloc" into two parts.  The first part should be
        # the authentication parameters, and the second part should be
        # the hostname and port.
        nls = p.netloc.split('@')

        # Set the hostname without any authentication parameters.
        if len(nls) == 1:
            _h = nls[0]

        elif len(nls) == 2:
            _h = nls[1]

        try:

            r = requests.get(p.scheme + '://' + _h + '/_up', timeout = 30.0)

            if r.status_code == 200:
                if r.json().get('status') == 'ok':
                    _alive = True

        except:
            pass

        if _alive == True:
            server = _temp

        else:

            reduced_urls = []

            for url in urls:
                if url != _temp:
                    reduced_urls.append(url)

            # Recursion, Yay!
            server = find_server(reduced_urls)

    return server


def get_session(url):
    """Get a session cookie from the CouchDB server.

    A session cookie value will be generated from the CouchDB server
    specified in the given URL.  The URL must contain a username and
    password as if HTTP basic authentication will be used.

    """
    session = {}

    # Parse the URL into its components.
    p = parse.urlsplit(url)

    # Split the "netloc" into two parts.  The first part should be the
    # authentication parameters, and the second part should be the
    # hostname and port.
    nls = p.netloc.split('@')

    if p.scheme in ('http', 'https'):

        if len(nls) == 2:

            ups = nls[0].split(':')

            if len(ups) == 2:

                head = {'Content-Type': 'application/x-www-form-urlencoded'}
                data = {'name': ups[0], 'password': ups[1]}

                try:

                    resp = requests.post(
                        p.scheme + '://' + nls[1] + '/_session',
                        headers = head,
                        data = data)
                    session['AuthSession'] = resp.cookies.get('AuthSession')

                except:
                    pass

    # If "AuthSession" key is found in the session dictionary, then
    # we can assume we found a valid CouchDB server.
    if 'AuthSession' in session:

        # Construct the URL without the basic authentication, setting
        # a URL attribute in the returned session dictionary.
        session['url'] = parse.urlunsplit(
            (p.scheme, nls[1], p.path, p.query, p.fragment))

    return session
