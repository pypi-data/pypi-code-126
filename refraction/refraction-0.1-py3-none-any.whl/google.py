"""
Sub-module for handling Google authentication & lookup stuff.

Note that Google API access setup uses a service account attached to a
Google Cloud project following [this
tutorial](https://developers.google.com/docs/api/quickstart/python).
"""

# Attempts at 2/3 dual compatibility:
from __future__ import print_function

__version__ = "0.1"

import sys

import flask # for flash

try:
    import google.oauth2.service_account
    import googleapiclient.discovery
    import googleapiclient.errors
    _AVAILABLE = True
except Exception:
    _AVAILABLE = False


_SHEETS = None
"""
The authenticated Google Sheets API service object that we can use to
read spreadsheet data. If it's `None`, that means that Google Sheets
integration was not requested, or `setup` hasn't been called yet.
"""

_PERMISSIONS_SHEET_NAME = "refraction-permissions"
"""
The name of the sub-sheet in which we'll search or view-creator names to
ensure permission management.
"""

_DOMAIN = ""
"""
The email domain (including '@') that can be combined with a username to
get an email address. Leave as an empty string to avoid checking for
emails in addition to usernames.
"""


def setup(config, extraScopes=None):
    """
    Sets up the module by making the Google API connection and submitting
    credentials. Before calling this function, other functions won't
    work. Any extra authorization scopes needed can be passed as a list
    of strings. The following configuration slots are used:

    - `GOOGLE_API_SERVICE_KEY_FILENAME`: must be the name of a service
        account key file. Get one after creating a service account in a
        Google Cloud project by:
        1. Go to APIs & Services -> Credentials and click on the service
            account.
        2. OR got to IAM & Admin -> Service Accounts and click on the
            service account.
        3. Once on the service account page, click the "Add Key" button.
            Note that you cannot re-download a previous key, and it's
            likely best to delete any previous keys if you need a new
            one. In theory, you should regularly rotate keys, although
            the automation to make that process smooth doesn't exist yet
            (TODO: that?).
    - `PERMISSIONS_SHEET_NAME`: if not present, value defaults to
        "refraction-permissions". This is the sub-sheet name that will be
        searched for usernames to establish whether a particular user can
        create a view of a sheet or not. Note that once a view is
        created, ANY user named in the viewed sub-sheet can view data, so
        you do not need to list all accounts who will use the view: just
        accounts that you want to be able to create views. This mechanism
        exists because otherwise, anyone with access to a document ID and
        who can guess a sub-sheet name could create a view of that
        sub-sheet and see data pertaining to their own account in that
        sub-sheet, even if they wouldn't normally have view access to
        that sub-sheet or view/edit access to the document. With this
        mechanism, only those who have edit access to the document (or
        who are otherwise listed in the permissions sub-sheet) can create
        a view of it.
    - `DOMAIN`: if not present, only usernames and not email addresses
        will be searched for when checking sheet permissions. If present,
        it should be the suffix (including '@') which can be added to a
        username to create an email address.
    """
    global _SHEETS, _PERMISSIONS_SHEET_NAME, _DOMAIN

    # Can't setup if required libraries are not installed
    if not _AVAILABLE:
        print(
            "Note: google and/or googleapiclient could not be imported;"
            " skipping Google integration setup."
        )
        _SHEETS = None
        return

    _PERMISSIONS_SHEET_NAME = config.get(
        "PERMISSIONS_SHEET_NAME",
        _PERMISSIONS_SHEET_NAME
    )

    _DOMAIN = config.get("DOMAIN", _DOMAIN)

    # Only set up a connection if a service key filename was provided
    skFile = config.get("GOOGLE_API_SERVICE_KEY_FILENAME")
    if skFile is None:
        _SHEETS = None
    else:
        creds = google.oauth2.service_account.Credentials\
            .from_service_account_file(
                filename=skFile,
                scopes=[ # list of permission scopes needed
                    'https://www.googleapis.com/auth/spreadsheets.readonly'
                ] + (extraScopes or [])
            )

        _SHEETS = googleapiclient.discovery.build(
            'sheets',
            'v4',
            credentials=creds
        )


def checkSheetViewPermissions(username, docID, domain=None):
    """
    Checks that the specified user has permission to create views of the
    Google sheet w/ the given document ID. Returns True if they do, and
    False if not. Flashes & prints an error message if it encounters an
    unexpected error trying to figure that out.

    Always returns False if the username is an empty string.

    Permissions are set via a sub-sheet named `_PERMISSIONS_SHEET_NAME`
    and every cell of that sheet is checked to see if it exactly matches
    either the given username, or the username plus the domain (default
    is to use the configuration file's `DOMAIN` entry provided via
    `setup`).
    """
    if username == '':
        return False

    if domain is None:
        domain = _DOMAIN

    vals = readSheetValues(docID, _PERMISSIONS_SHEET_NAME, quiet=True)
    if vals is None: # no such sub-sheet
        return False

    match = set([username, username + domain])
    for row in vals:
        for entry in row:
            if entry in match:
                return True

    return False


def readSheetValues(docID, sheetName, quiet=False):
    """
    Reads all[^1] values from a specific sub-sheet of the Google Sheet
    w/ the given document ID. The sheet to read from must be viewable by
    the service account used to authenticate when `setup` was called.
    You can see the email to share with in the APIs & Services ->
    Credentials pane of the Google Cloud project that the service
    account is attached to.

    Returns a list-of-lists-of-strings where each sub-list is a row. The
    number of columns/rows depends on the extents of data in the sheet,
    not on the total number of empty cells.

    If there's an error trying to fetch the data, the error details will
    be flashed & printed, and the return value will be None. However, if
    `quiet` is set to True, nothing is flashed or printed in this case
    (although the return value will still be None).

    If the sheet to be read is empty, an empty list will be returned.

    [^1]: To simplify the read, columns beyond the 17576th will not be
    included in the results.
    """
    if _SHEETS is None:
        if not quiet:
            msg = (
                "Cannot access Google Sheets data because setup was not"
                " performed or no service account key file was provided."
            )
            flask.flash(msg)
            print(msg, file=sys.stderr)
        return None

    try:
        response = _SHEETS.spreadsheets().values().get(
            spreadsheetId=docID,
            range=sheetName + '!A1:ZZZ'
        ).execute()
    except googleapiclient.errors.HttpError as err:
        if not quiet:
            msg = "Error attempting to access sheet values:\n" + str(err)
            flask.flash(msg)
            print(msg, file=sys.stderr)
        return None

    # Won't even be a 'values' key for a sheet w/ no data in it
    return response.get('values', [])


if __name__ == '__main__':
    setup({
        "GOOGLE_API_KEY_FILENAME": \
            "refraction-wellesley-pmawhort-944b9532af7d.json",
        "DOMAIN": "@wellesley.edu"
    })
    print(
        readSheetValues(
            # Test spreadsheet in shared drive folder shared w/ the bot
            '1wVZBBIaBdBYS9CdzyAsqWcwEaYDW00d81JplMyUzILU',
            # Public self-owned test sheet shared w/ the bot
            #'1s7NNFT12B8gWOSCc9v_qt9eUdV8PQ44FCH3zuFlTXGA',
            "sheet"
        )
    )
