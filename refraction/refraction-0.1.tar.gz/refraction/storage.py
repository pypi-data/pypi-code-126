"""
Long-term storage & caching using Redis.
"""

# Attempts at 2/3 dual compatibility:
from __future__ import print_function

__version__ = "0.2"

import sys, os, shutil, subprocess, threading, copy
import time, datetime
import traceback
import base64, csv
import shlex
import re

from flask import json

import flask, werkzeug.datastructures, redis

from . import google, timeUtils

# Python 2/3 dual compatibility
if sys.version_info[0] < 3:
    reload(sys) # noqa F821
    sys.setdefaultencoding('utf-8')
    import socket
    ConnectionRefusedError = socket.error
    IOError_or_FileNotFoundError = IOError
    OSError_or_FileNotFoundError = OSError
else:
    IOError_or_FileNotFoundError = FileNotFoundError
    OSError_or_FileNotFoundError = FileNotFoundError


#-----------#
# Constants #
#-----------#

SCHEMA_VERSION = "1"
"""
The version for the schema used to organize information under keys in
Redis. If this changes, all Redis keys will change.
"""

ENCODING = "utf-8"
"""
The text encoding used for writing data given as 'unicode' in Python 2,
and used for reading all data.

TODO: Specify via OS and/or a config variable...
"""

PATH_DISALLOWED = re.compile(r"[^\w_. -]")
"""
A regular expression for finding characters in paths which we aren't
certain are safe as part of a file or directory name. Includes
*anything* which is not a word character, a dash, an underscore, a
period, or a space.
"""


#-----------#
# Utilities #
#-----------#

def ensureDirectory(target):
    """
    makedirs 2/3 shim.
    """
    if sys.version_info[0] < 3:
        try:
            os.makedirs(target)
        except OSError:
            pass
    else:
        os.makedirs(target, exist_ok=True)


def removeAll(sequence, item):
    """
    Removes all items from a given sequence that match (using ==) the
    specified item. Edits the sequence in-place (so doesn't work on a
    tuple, for example).

    ## Examples

    >>> L = [1, 2, 3, 2, 3, 4]
    >>> removeAll(L, 2)
    >>> L
    [1, 3, 3, 4]
    >>> removeAll(L, 1)
    [3, 3, 4]
    >>> removeAll(L, 3)
    [4]
    >>> PL = [ [1, 2], [3, 4], [1, 2], [1, 5] ]
    >>> removeAll(PL, [1, 2])
    >>> PL
    [[3, 4], [1, 5]]
    >>> removeAll(PL, [3, 5]) # no error if it's not there
    >>> PL
    [[3, 4], [1, 5]]
    >>> removeAll(PL, [3, 4])
    >>> PL
    [[1, 5]]
    """
    # Find indices at which to remove items
    remove = []
    for idx in range(len(sequence)):
        if sequence[idx] == item:
            remove.append(idx)

    # Remove each of those
    adjust = 0
    for r in remove:
        sequence.pop(r - adjust)
        adjust += 1


#--------------------#
# Filename functions #
#--------------------#

def unusedFilename(target):
    """
    Checks whether the target already exists, and if it does, appends .N
    before the file extension, where N is the smallest positive integer
    such that the returned filename is not the name of an existing file.
    If the target does not exists, returns it.
    """
    n = 1
    backup = target
    base, ext = os.path.splitext(target)
    while os.path.exists(backup):
        backup = base + "." + str(n) + ext
        n += 1

    return backup


def makeWayFor(target):
    """
    Given that we're about to overwrite the given file, this function
    moves any existing file to a backup first, numbering backups starting
    with .1. The most-recent backup will have the largest backup number.

    After calling this function, the given target file will not exist,
    and so new material can be safely written there.

    This function returns the filename for the backup file it created, or
    `None` if no backup was made (because the file already didn't exist).
    """
    backup = unusedFilename(target)
    if backup != target:
        shutil.move(target, backup)
        return backup
    else:
        return None


def uploadFilename(dataInfo):
    """
    Returns the filename used to store data for the specified data
    upload. Uses the `DATA_DIR` configuration variable.

    Creates the associated user if that user didn't already exist.
    """
    creator = dataInfo["creator"]
    userInfo = getUserInfo(creator, create=True)

    return os.path.join(
        _CONFIG.get("DATA_DIR", '.'),
        userInfo["path"],
        dataInfo["name"] + '.' + dataInfo["format"].lower()
    )


def backupPath(dataInfo, backupFilename):
    """
    Returns the full file path for a backup file given the data info for
    that upload plus the backup filename as stored in the "backups" list
    for that same upload.

    Creates the associated user if that user didn't already exist.
    """
    creator = dataInfo["creator"]
    userInfo = getUserInfo(creator, create=True)

    return os.path.join(
        _CONFIG.get("DATA_DIR", '.'),
        userInfo["path"],
        backupFilename
    )


#---------------------#
# Redis key functions #
#---------------------#

def redisKey(suffix):
    """
    Given a key suffix, returns a full Redis key which includes
    "refraction:<version>" where version is the schema version (see
    `SCHEMA_VERSION`).
    """
    return "refraction:" + SCHEMA_VERSION + ":" + suffix


def redisKeySuffix(key):
    """
    Returns the part of a Redis key that wasn't added by the `redisKey`
    function.
    """
    return key[len(redisKey("")):]


def viewKey(creator, viewName):
    """
    The redis key for storing view info. Each view is specific to a
    particular creator and its name must be unique among that creator's
    views.
    """
    return redisKey("v:" + creator + ":" + viewName)


def userKey(username):
    """
    The redis key for storing user info.
    """
    return redisKey("u:" + username)


def userPathKey(userPath):
    """
    The redis key for storing a user's path, which is usually just their
    username but if special characters are included it may be different.

    The argument is that path (NOT their username), and the values
    stored are usually just empty strings to indicate that that path key
    has been taken.
    """
    return redisKey("upk:" + userPath)


def dataKey(creator, dataName):
    """
    The redis key for storing uploaded data + metadata. Each data upload
    is specific to a particular creator and its name must be unique
    among that creator's data uploads.
    """
    return redisKey("d:" + creator + ":" + dataName)


#------------------------------#
# Base info fetching functions #
#------------------------------#

def getAdminInfo():
    """
    Loads the app-wide admin info from the JSON file specified by the
    current configuration (or returns a cached version if the file
    hasn't been modified since we last loaded it).

    Returns None if the file doesn't exist or can't be parsed.
    """
    filename = _CONFIG["ADMIN_FILE"]
    try:
        result = loadOrGetCached(filename, view=AsJSON)
    except Exception:
        flask.flash("Failed to read admin info file!")
        tb = traceback.format_exc()
        print(
            "Failed to read admin info file:\n" + tb,
            file=sys.stderr
        )
        result = None

    return result


class NotAvailable:
    """
    Used to represent the fact that info wasn't available when `None`
    could be a valid value for the info in question.
    """
    def __init__(self):
        raise NotImplementedError(
            "Cannot instantiate NotAvailable (just use the class itself"
            " as a singleton value)."
        )


def readInfoAsJson(key):
    """
    Reads info stored in redis as JSON, returning a Python object parsed
    from the data stored under the provided key. Returns `NotAvailable`
    if there's any error encountered, including if there's no info under
    that key. In that case, it will both flash a message using flask and
    print details to stderr.
    """
    try:
        stored = _REDIS.get(key)
        if stored is None:
            msg = "No info at '{}'.".format(key)
            flask.flash(msg)
            print(msg, file=sys.stderr)
            return NotAvailable
        else:
            return json.loads(stored)
    except Exception:
        flask.flash(
            "Failed to read info at '{}'!".format(key)
        )
        tb = traceback.format_exc()
        print(
            "Failed to read info at '{}':\n{}".format(
                key,
                tb
            ),
            file=sys.stderr
        )
        return NotAvailable


def writeBlank(key):
    """
    Writes an empty string to the specified redis key, returning True on
    success and False on failure (in which case it also flashes/prints a
    message).
    """
    try:
        _REDIS.set(key, "")
        return True
    except Exception:
        flask.flash(
            "Failed to write blank at '{}'!".format(key)
        )
        tb = traceback.format_exc()
        print(
            "Failed to write blank at '{}':\n{}".format(
                key,
                tb
            ),
            file=sys.stderr
        )
        return False


def writeInfoAsJson(key, object):
    """
    Writes a Python object that can be converted to JSON as a JSON
    string in redis under the specified key, returning True on success
    and False on failure (in which case it also flashes a message in
    flask and prints an error message to stderr).
    """
    try:
        _REDIS.set(key, json.dumps(object))
        return True
    except Exception:
        flask.flash(
            "Failed to write info at '{}'!".format(key)
        )
        tb = traceback.format_exc()
        print(
            "Failed to write info at '{}':\n{}".format(
                key,
                tb
            ),
            file=sys.stderr
        )
        return False


def infoExists(key):
    """
    Returns True if there's some info stored under the given key, and
    False otherwise. Flashes/prints a message and returns None if
    there's some kind of error trying to access redis.
    """
    try:
        return bool(_REDIS.exists(key))
    except Exception:
        flask.flash(
            "Failed to check for info at '{}'!".format(key)
        )
        tb = traceback.format_exc()
        print(
            "Failed to check for info at '{}':\n{}".format(
                key,
                tb
            ),
            file=sys.stderr
        )
        return None


def deleteInfo(key):
    """
    Deletes the information stored under the specified redis key. Returns
    True on success and flashes/prints a message and returns False if
    there's any kind of error.

    If the key already doesn't exist, it still returns True.
    """
    try:
        _REDIS.delete(key)
        return True
    except Exception:
        flask.flash(
            "Failed to delete info at '{}'!".format(key)
        )
        tb = traceback.format_exc()
        print(
            "Failed to delete info at '{}':\n{}".format(
                key,
                tb
            ),
            file=sys.stderr
        )
        return False


def getUserInfo(username, create=False):
    """
    Looks up a user's info. Returns None and prints/flashes an error
    message if the user info cannot be read for any reason. If `create`
    is set to `True`, then new info will be created, stored, and returned
    if the user info doesn't exist. The user info is a dictionary with
    the following slots:

    - 'username': The username, which will match their CAS login.
    - 'path': A unique-to-this-user string that can be used as a path
        component. Normally just the username, with special characters
        replaced by underscores, although if that creates a collision, a
        unique path will be chosen using a suffix.
    - 'bookmarked': A list of creator/view 2-element lists specifying
        views which this user has bookmarked. These appear on the user's
        default landing page for quick access, and are set automatically
        the first time a view is accessed. They can be manually removed
        by the user.
    - 'accessed': A dictionary mapping creator usernames to dictionaries
        mapping view names to timestamps indicating when they were most
        recently accessed.
    - 'managing': A list of creator/view pairs (2-element lists)
        containing all views that can be managed by this user, including
        all views created by this user. This user should be listed in
        the 'admins' list of each of these views; that info is
        considered authoritative for access while this info is just a
        convenience.
    - 'uploads': A list of creator/name pairs (2-element lists)
        containing all data uploads that this user has either view or
        edit access to, including all uploads they created. Note that
        the individual creator/viewer/editor lists of each data item
        actually control access; these lists are just for convenience.
    """
    # If the user isn't registered, create their entry and return that
    key = userKey(username)
    if not _REDIS.exists(key):
        if create:
            return createUser(username)
        else:
            msg = "User '{}' does not exist.".format(username)
            flask.flash(msg)
            print(msg, file=sys.stderr)
            return None

    # Otherwise read their entry & return None on error:
    result = readInfoAsJson(key)
    if result is NotAvailable:
        return None
    else:
        return result


def setUserInfo(username, info):
    """
    Sets user info, overwriting any previous user info. The `info`
    argument should be a user info object (see `getUserInfo`); it will
    be converted to a JSON string automatically. This function returns
    True on success and False on failure (in which case it also prints
    and flashes error messages).
    """
    return writeInfoAsJson(userKey(username), info)


def getViewInfo(creator, viewName):
    """
    Looks up a view's info. Returns None and prints/flashes an error
    message if the view info cannot be read for any reason. The view
    info is a dictionary with the following slots:

    - 'creator': The username of the user who created it.
    - 'name': The view name (unique within views created by that user).
    - 'contact': A string (could be an email address, a phone number, or
        whatever you want) specifying who to contact if there's an issue
        with the view.
    - 'admins': A list of usernames for users who can administer the
        view. The creator need not be listed and always has access.
        Admins can change anything about the view, including adding or
        removing other admins or even themselves. However, to change the
        data source for a view, an admin must have access to the new
        data source (i.e., their account must have at least view access
        to the Google sheet, or they must be listed as at least a viewer
        of an uploaded CSV file).
    - 'source': The data source for the view. This is a list of
        strings, where the first string specifies the type of source
        (see `SOURCE_TYPES` for the list of supported types). The
        remaining strings specify how to access the data, and are
        dependent on the source type.
    - 'index': The column name to match against user IDs that determines
        who can use the view and what info they will see. Each viewer
        (besides admins) will only be shown info from the first row in
        which their user ID is listed in the specified column. If there
        are no such rows, they will see a generic "you don't have info
        for this view" message, and if there are multiple matching rows,
        the view will be rendered using all of them (although some views
        might only use the first row and include a warning message if
        there are multiple).
    - 'suffix': A string to be appended to the username to get the value
        that will be matched against the index column. A default may be
        specified in the configuration file which will be used whenever
        a new view is created. Typically a domain is used, when data
        sources contain, e.g., email addresses rather than just
        usernames.
    - 'header': An integer indicating the number of rows beyond the
        first row to include in everyone's view. Note that the values in
        the index column for these rows MUST be blank, or the rows will
        not be shown and a warning message will be shown to admins
        looking at the view; this is to prevent accidentally
        broadcasting some particular user's data to everyone. The value
        in the first column of an included header row is used as a key
        to retrieve that header info; see `fetchUserView` for details.
    - 'template': Which template will be used to render this view (a
        string naming one of the built-in templates). Templates can be
        added by placing them in the `TEMPLATE_DIRECTORY` specified in
        the config file. Note that most templates will want to extend the
        built-in `'bare.j2'` template by using the line:
        `{% extends "bare.j2" %}` and then putting their content into
        `{% block body %}`. If this field is blank, a default template
        will be used (see `view.j2` in the `templates` directory of this
        package). An example custom template can be found in the
        `refraction/rundir/templates` directory.
    """
    result = readInfoAsJson(viewKey(creator, viewName))
    if result is NotAvailable:
        return None
    else:
        return result


def setViewInfo(creator, viewName, info):
    """
    Sets view info, overwriting any previous view info for that view.
    The `info` argument should be a view info object (see
    `getViewInfo`); it will be converted to a JSON string automatically.
    This function returns True on success and False on failure (in which
    case it also prints and flashes error messages).
    """
    return writeInfoAsJson(viewKey(creator, viewName), info)


def getUploadInfo(creator, dataName):
    """
    Gets a data object which represents uploaded data that can be used
    as a data source for a view. Returns `None` and flashes/prints a
    warning message if the data can't be retrieved or parsed. The return
    value is actually a dictionary with the following slots:

    - 'creator': The creator of this data object.
    - 'name': The unique (per creator) name for this data object.
    - 'editors': A list of usernames specifying which users besides the
        creator can edit the data, including uploading new versions.
        Note that version history is NOT tracked automatically, so these
        users can effectively delete the data. There is no way to deny
        the creator edit access; if this is desired it's best to clone
        the data under another user's account and ask the original
        creator to delete it.
    - 'viewers': A list of usernames specifying which users besides the
        creator can view (but not necessarily edit) the data. Editors
        automatically have view access so they don't need to be listed
        twice.
    - 'format': A string indicating the data format, like 'CSV' or
        'TSV'.
    - 'backups': A list of filenames specifying different versions of the
        upload that have been backed up, excluding the current version
        (whose filename you can get using `uploadFilename`). These are
        filenames only, not full paths.
    """
    result = readInfoAsJson(dataKey(creator, dataName))
    if result is NotAvailable:
        return None
    else:
        return result


def setUploadInfo(creator, dataName, dataObj):
    """
    Overwrites existing data, including metadata like the viewers/editors
    lists (see `getUploadInfo` for the structure, which the provided
    `dataObj` must match). Returns True on success and False on failure.
    """
    return writeInfoAsJson(dataKey(creator, dataName), dataObj)


#---------------------------#
# Common fetch/set patterns #
#---------------------------#

def logAccess(user, creator, view):
    """
    Logs the fact that a user accessed a particular view, storing that
    info in the user's info and also bookmarking that view if this is
    the first time they've accessed it. Note that this should probably
    only be called for access attempts that succeed (i.e., where the
    viewer actually has data they can view) to avoid polluting the
    user's bookmarks, since it's not intended to be a strict access log
    of what the user attempted to access.

    If the user didn't already have registered info, their info will be
    created.

    The current time when this function is called is set as the access
    time.
    """
    info = getUserInfo(user, create=True)
    access = info['accessed']

    # Check for previous access and auto-bookmark if not
    prevTS = access.get(creator, {}).get(view)
    if prevTS is None:
        info["bookmarked"].append([creator, view])

    access.setdefault(creator, {})[view] = timeUtils.timeString()

    setUserInfo(user, info)


def removeBookmark(user, creator, view):
    """
    Removes a particular view (created by a specific creator) from the
    specified user's bookmarks. Does nothing if that view isn't already
    bookmarked.

    The user must already be registered.
    """
    info = getUserInfo(user, create=False)

    check = [creator, view]
    info["bookmarked"] = list(
        filter(lambda x: x != check, info["bookmarked"])
    )

    # Update the user info w/ the edited information
    setUserInfo(user, info)


def noteManager(user, creator, view, removed=False):
    """
    Notes that the specified user has been given manager status on the
    specified view (created by the specified creator). This does not
    actually give them permission; instead it should be called after
    editing the view info to set them as a manager. Set `removed` to
    True (default is False) to note removal rather than instatement.

    No error messages are generated even when noting a user as a manager
    who has already been noted or when removing a manger note that
    doesn't exist. If a user has been noted as a manager multiple times,
    noting their removal once will remove all such notes.

    Creates a new user info entry if it has to.
    """
    info = getUserInfo(user, create=True)

    entry = [creator, view]

    if removed:
        # Remove all copies from the list
        info["managing"] = list(
            filter(lambda x: x != entry, info["managing"])
        )
    else:
        # Add entry at the end of the list
        info["managing"].append(entry)

    # Update the user info w/ the edited information
    setUserInfo(user, info)


def noteUpload(user, creator, dataName, removed=False):
    """
    Notes that the specified user has been given view or edit status on
    the specified data upload (created by the specified creator). This
    does not actually give them permission; instead it should be called
    after editing the data info to set them as a viewer/editor (or when
    they create a new upload). Set `removed` to True (default is False)
    to note removal rather than instatement.

    No error messages are generated even when noting a user as having
    access who has already been noted or when removing an access note
    that doesn't exist. If a user has been noted as having access
    multiple times, noting their removal once will remove all such notes.

    Creates a new user info entry if it has to.
    """
    info = getUserInfo(user, create=True)

    entry = [creator, dataName]

    if removed:
        # Remove all copies from the list
        info["uploads"] = list(
            filter(lambda x: x != entry, info["uploads"])
        )
    else:
        # Add entry at the end of the list
        info["uploads"].append(entry)

    # Update the user info w/ the edited information
    setUserInfo(user, info)


def createUser(username):
    """
    Creates a new user info entry for the user with the specified
    username. If that user already had info, it gets overwritten with
    blank info.

    Returns the info dictionary it creates (see `getUserInfo`). If some
    kind of error is encountered trying to create the user, it will
    print/flash a message about that and return None.
    """
    # First delete any old path info for this username
    if infoExists(userKey(username)):
        oldInfo = getUserInfo(username)
        oldPath = userPathKey(oldInfo["path"])
        deleteInfo(userPathKey(oldPath))

    # Find a unique path for this user in case escaping their username
    # for use in file paths leads to a collision with another user's
    # username (highly unlikely, but maybe not impossible?)
    path = PATH_DISALLOWED.sub('_', username)
    if infoExists(userPathKey(path)):
        tryPath = path + '.1'
        suffix = 1
        while infoExists(userPathKey(tryPath)):
            suffix += 1
            tryPath = path + '.' + str(suffix)
        path = tryPath

    # Build our new info object & store it
    info = {
        'username': username,
        'path': path,
        'bookmarked': [],
        'accessed': {},
        'managing': [],
        'uploads': [],
    }
    succeeded = setUserInfo(username, info)
    if not succeeded:
        return None

    # Also save the new path object
    key = userPathKey(path)
    succeeded = writeBlank(key)
    if not succeeded:
        return None

    return info


def messageWithValue(message, value):
    """
    Boilerplate for formatting a value into an error message.
    """
    if message and message[-1] in ' \n':
        sep = ''
    else:
        sep = ' '
    return message + sep + "You provided:\n{}".format(repr(value))


def typeCheckViewInfo(
    creator,
    name,
    admins,
    source,
    contact,
    index,
    suffix,
    header,
    template
):
    """
    Checks that each component of a view being created/updated has the
    right type. Performs the following checks, raising a `TypeError` if
    any fail:

    - `creator` must be a string
    - `name` must be a string
    - `admins` must be a list of strings (it may be empty)
    - `source` must be a list of strings (and while not a type
        constraint, the first string must be a valid source type from
        `SOURCE_TYPES`, otherwise a `ValueError` will be raised)
    - `contact` must be a string
    - `index` must be a string
    - `suffix` must be a string
    - `header` must be an integer
    - `template` must be a string (use empty string for default template)
    """
    if not isinstance(creator, str):
        raise TypeError(
            messageWithValue("A view creator must be a string.", creator)
        )

    if not isinstance(name, str):
        raise TypeError(
            messageWithValue("A view name must be a string.", name)
        )

    if not isinstance(admins, list):
        raise TypeError(
            messageWithValue("View admins must be a list.", admins)
        )

    if not all(isinstance(elem, str) for elem in admins):
        raise TypeError(
            messageWithValue("Each view admin must be a string.", admins)
        )

    if not isinstance(source, list):
        raise TypeError(
            messageWithValue("A view source must be a list.", source)
        )

    if not all(isinstance(elem, str) for elem in source):
        raise TypeError(
            messageWithValue(
                "Each element of a view source must be a string.",
                source
            )
        )

    if len(source) < 1:
        raise ValueError(
            messageWithValue(
                "A view source must include at least a source type.",
                source
            )
        )

    if source[0] not in SOURCE_TYPES:
        raise ValueError(
            messageWithValue(
                (
                    "The view source type (first entry in the source"
                    " list) must be one of:\n  "
                ) + '\n  '.join(SOURCE_TYPES) + '\n',
                source[0]
            )
        )

    if not isinstance(contact, str):
        raise TypeError(
            messageWithValue(
                "The view contact info must be a string.",
                contact
            )
        )

    if not isinstance(index, str):
        raise TypeError(
            messageWithValue(
                "The view index column must be a string.",
                index
            )
        )

    if not isinstance(suffix, str):
        raise TypeError(
            messageWithValue("The view suffix must be a string.", suffix)
        )

    if not isinstance(header, int):
        raise TypeError(
            messageWithValue(
                "The view header rows count must be a string.",
                header
            )
        )

    if not isinstance(template, str):
        raise TypeError(
            messageWithValue(
                "The view template must be a string.",
                template
            )
        )


def createView(
    creator,
    viewName,
    source,
    admins=None,
    contact='',
    index="username",
    suffix=None,
    header=0,
    template=""
):
    """
    Creates a new view with the given name, associated with the given
    creator. The source argument must be a list that starts with a valid
    data source type (see `SOURCE_TYPES`) and whose remaining values
    will be given to the fetcher for that type, along with the
    view creator's username, to fetch the data. The rest of the arguments
    are optional, and override defaults for various aspects of the view.

    If a view with the specified name already exists, this function
    flashes/prints an error message and returns False. Otherwise it
    creates the view and returns True.

    The default admins list is an empty list, the default contact info is
    an empty string, the default index is `'username'`, the default
    suffix is the config file's `DOMAIN` value, or an empty string if
    that is not set, the default number of extra header rows is zero, and
    the default template is an empty string.

    `typeCheckViewInfo` is used to check that data has the proper types.
    """
    # TODO: There's a race condition between our check here and set
    # below; could use a redis pipeline to avoid that...
    if infoExists(viewKey(creator, viewName)):
        msg = "Invalid view name: {}. Name already in use.".format(
            repr(viewName)
        )
        flask.flash(msg)
        print(msg, file=sys.stderr)
        return False

    if admins is None:
        admins = []

    if suffix is None:
        suffix = _CONFIG.get("DOMAIN", '')

    # Check types
    typeCheckViewInfo(
        creator,
        viewName,
        admins,
        source,
        contact,
        index,
        suffix,
        header,
        template
    )

    info = {
        'creator': creator,
        'name': viewName,
        'contact': contact,
        'admins': admins,
        'source': source,
        'index': index,
        'suffix': suffix,
        'header': header,
        'template': template,
    }
    setViewInfo(creator, viewName, info)
    noteManager(creator, creator, viewName)
    return True


def updateView(
    creator,
    viewName,
    admins=None,
    source=None,
    contact=None,
    index=None,
    suffix=None,
    header=None,
    template=None
):
    """
    Updates one or more fields in a view. The default value for each
    parameter is None, and if these are left unchanged, those fields
    won't be updated from their current values. See `getViewInfo` for a
    description of what each field means. Returns True if the view is
    successfully updated, or False if the view does not exist and is
    therefore not updated.

    Automatically updates user info for any users added to or removed
    from the admins list.

    Uses `typeCheckViewInfo` to check that values have correct types.
    """
    # TODO: Fix race condition?
    info = getViewInfo(creator, viewName)
    if info is None:
        return False

    # Check types, ignoring defaults
    typeCheckViewInfo(
        creator,
        viewName,
        admins if admins is not None else [],
        source if source is not None else ['upload'],
        contact if contact is not None else '',
        index if index is not None else '',
        suffix if suffix is not None else '',
        header if header is not None else 0,
        template if template is not None else ''
    )

    if admins is not None:
        # Figure out who is being added/removed
        old = set(info["admins"])
        new = set(admins)
        added = new - old
        removed = old - new

        for user in added:
            noteManager(user, creator, viewName)

        for user in removed:
            noteManager(user, creator, viewName, removed=True)

        # Update the admins list
        info["admins"] = admins

    if source is not None:
        info["source"] = source

    if contact is not None:
        info["contact"] = contact

    if index is not None:
        info["index"] = index

    if suffix is not None:
        info["suffix"] = suffix

    if header is not None:
        info["header"] = header

    if template is not None:
        info["template"] = template

    setViewInfo(creator, viewName, info)
    return True


def deleteView(creator, name):
    """
    Permanently deletes the view with the given creator/name. Also
    removes that view's info from the managing list of all associated
    admins & the creator, although it does not remove access records.

    Returns True on success and False on failure, in which case it will
    print & flash a message about the failure. Attempting to delete a
    non-existent view is an error.
    """
    info = getViewInfo(creator, name)
    if info is None:
        msg = "Cannot delete view {}/{}: that view doesn't exist.".format(
            creator,
            name
        )
        flask.flash(msg)
        print(msg, file=sys.stderr)
        return False

    # Remove from each associated manager
    for user in info["admins"]:
        noteManager(user, creator, name, removed=True)

    # Remove even from the creator
    noteManager(creator, creator, name, removed=True)

    return deleteInfo(viewKey(creator, name))


def addAdmin(user, creator, viewName):
    """
    Adds the specified user as an admin for the view with the given name
    created by the given creator.

    Also updates their user data to list that view as one that they're
    administering.

    Does nothing if the user is already an admin for that view.
    """
    info = getViewInfo(creator, viewName)
    if user in info["admins"]:
        return

    info["admins"].append(user)
    noteManager(user, creator, viewName)

    setViewInfo(creator, viewName, info)


def removeAdmin(user, creator, viewName):
    """
    Removes the specified user from the admin list for the given view.
    Does nothing if they weren't on the list. Also updates their user
    profile to indicate they're no longer an admin for that view.

    The creator of a view cannot be removed as an admin; they always
    retain admin privileges for the view.
    """
    info = getViewInfo(creator, viewName)
    admins = info["admins"]
    if user not in admins:
        return

    info["admins"] = list(filter(lambda x: x != user, admins))

    noteManager(user, creator, viewName, removed=True)

    setViewInfo(creator, viewName, info)


def typeCheckUploadInfo(
    creator,
    name,
    format,
    editors,
    viewers,
    dataOrUpload=NotAvailable
):
    """
    Type checks arguments for creating/updating an upload. Checks the
    following, raising a `TypeError` if a check fails:

    - `creator` must be a string.
    - `name` must be a string.
    - `format` must be a string, and it must also be one of the
        `UPLOAD_FORMATS` or else a `ValueError` will be raised.
    - `editors` must be a (possibly empty) list of strings.
    - `viewers` must be a (possibly empty) list of strings.
    - `dataOrUpload` must be one of:
        * a string
        * a `bytes` object (only in Python version 3)
        * a `unicode` object (only in Python version 2)
        * a `werkzeug.datastructures.FileStorage` object
        * `NotAvailable` (the default, which can be used to avoid
            type-checking this field if there is no value as with
            `updateUpload`).

    Note that this does NOT check that the creator/name combo is unique.
    """
    if not isinstance(creator, str):
        raise TypeError(
            messageWithValue("An upload creator must be a string.", creator)
        )

    if not isinstance(name, str):
        raise TypeError(
            messageWithValue("An upload name must be a string.", name)
        )

    if not isinstance(format, str):
        raise TypeError(
            messageWithValue("An upload format must be a string.", name)
        )

    if format not in UPLOAD_FORMATS:
        raise ValueError(
            messageWithValue(
                (
                    "The upload format must be one of the following:\n  "
                  + '\n  '.join(UPLOAD_FORMATS)
                  + '\n'
                ),
                format
            )
        )

    # Check editors & viewers the same way
    for (name, var) in [("editor", editors), ("viewer", viewers)]:
        if not isinstance(var, list):
            raise TypeError(
                messageWithValue(
                    "Upload {}s must be a list.".format(name),
                    var
                )
            )

        if not all(isinstance(elem, str) for elem in var):
            raise TypeError(
                messageWithValue(
                    "Each upload {} must be a string.".format(name),
                    var
                )
            )

    allowed = [werkzeug.datastructures.FileStorage, str]
    allowedNames = ["werkzeug.datastructures.FileStorage", "str"]
    if sys.version_info < (3, 0):
        allowed.append(unicode) # noqa F821
        allowedNames.append("unicode")
    else:
        allowed.append(bytes)
        allowedNames.append("bytes")

    if (
        dataOrUpload is not NotAvailable
    and not isinstance(dataOrUpload, tuple(allowed))
    ):
        raise TypeError(
            messageWithValue(
                (
                    "The data or upload must be `NotAvailable` to skip"
                  + " this check, or must be one of the following"
                  + " types:\n  "
                  + '\n  '.join(allowedNames)
                ),
                dataOrUpload
            )
        )


def createUpload(
    creator,
    name,
    dataOrUpload,
    format="CSV",
    editors=None,
    viewers=None,
):
    """
    Creates a new data upload object, storing a bit of metadata like the
    creator and a data name along with the provided data. The data must
    be a string or bytes object, OR a
    `werkzeug.datastructures.FileStorage` object that we can save
    directly as a file.

    A list of usernames may be provided to give additional users edit
    permissions for the data object, and a second list of usernames for
    view permissions may also be provided. Users in these lists will
    have their user info updated.

    The data format should be specified; 'CSV' is the default, which
    implies that the data is a multi-line string that can be interpreted
    using the `csv` module's default format (use 'TSV' if the data is in
    'excel-tab' format instead).

    The upload name may only contain words, dashes, underscores, periods,
    and spaces; no other special characters are allowed.

    Returns True on success, or False if a data object with the given
    name and creator already exists or if the name is invalid (in those
    cases, no changes are made and an error message is flashed/printed).
    """
    # TODO: There's a race condition between our check here and set
    # below; could use a redis pipeline to avoid that...
    if infoExists(dataKey(creator, name)):
        msg = "Invalid upload name: {}. Name is already in use.".format(
            repr(name)
        )
        flask.flash(msg)
        print(msg, file=sys.stderr)
        return False

    if PATH_DISALLOWED.sub('_', name) != name:
        msg = (
            "Invalid upload name: {}. Only alphanumeric characters plus"
            " dash, underscore, period, and space are allowed."
        ).format(repr(name))
        flask.flash(msg)
        print(msg, file=sys.stderr)
        return False

    if editors is None:
        editors = []

    if viewers is None:
        viewers = []

    # Check types
    typeCheckUploadInfo(
        creator=creator,
        name=name,
        format=format,
        editors=editors,
        viewers=viewers,
        dataOrUpload=dataOrUpload
    )

    # Note relationship for creator
    noteUpload(creator, creator, name)

    # Note relationship for each editor/viewer
    for ed in editors:
        noteUpload(ed, creator, name)

    for vw in viewers:
        noteUpload(vw, creator, name)

    # Create our new metadata
    info = {
        'creator': creator,
        'name': name,
        'editors': editors,
        'viewers': viewers,
        'format': format,
        'backups': []
    }

    # Store the data on disk
    backup = replaceData(info, dataOrUpload)
    if backup is not None:
        flask.flash(
            (
                "Note: upload {}/{} existed previously and was deleted;"
                " old backups are being retained."
            ).format(creator, name)
        )
        info["backups"].append(backup)

    # Now that the file exists on disk, we store the metadata in REDIS
    setUploadInfo(creator, name, info)

    return True


def updateUpload(
    creator,
    name,
    format=None,
    editors=None,
    viewers=None,
    backups=None
):
    """
    Works like `updateView` but for a data upload. As with `updateView`
    the return value indicates success or failure. Note that this
    function will automatically update the user info for any added or
    removed editors or viewers.

    However, this function notably cannot modify the stored data, just
    metadata. Use `replaceData` for uploading a new version of the
    underlying data.

    This function does not flash or print any messages on failure.
    """
    # TODO: Fix race condition?
    info = getUploadInfo(creator, name)
    if info is None:
        return False

    # Type check stuff, using safe defaults for unchanged values
    typeCheckUploadInfo(
        creator=creator,
        name=name,
        format=format if format is not None else "CSV",
        editors=editors or [],
        viewers=viewers or [],
        dataOrUpload=NotAvailable # no dataOrUpload to check
    )

    if format is not None:
        info["format"] = format

    alreadyPermitted = set(info["editors"]) | set(info["viewers"])
    newEditors = set()
    newViewers = set()

    if editors is not None:
        newEditors = set(editors)
        info["editors"] = editors
    else:
        newEditors = set(info["editors"])

    if viewers is not None:
        newViewers = set(viewers)
        info["viewers"] = viewers
    else:
        newViewers = set(info["viewers"])

    if backups is not None:
        info["backups"] = backups

    # Actually store the new info
    setUploadInfo(creator, name, info)

    # Figure out who has been added/removed & update their user data
    allNew = newEditors | newViewers
    added = allNew - alreadyPermitted
    removed = alreadyPermitted - allNew

    for user in added:
        noteUpload(user, creator, name)

    for user in removed:
        noteUpload(user, creator, name, removed=True)

    return True


def deleteUpload(creator, name):
    """
    Permanently deletes the upload with the given creator/name. This
    includes deleting the uploaded data and *ALL* backups.

    Returns True on success and False on failure, in which case it will
    print & flash a message about the failure.
    """
    info = getUploadInfo(creator, name)

    if info is None:
        msg = "Cannot delete upload {}/{}: it does not exist.".format(
            creator,
            name
        )
        flask.flash(msg)
        print(msg, file=sys.stderr)
        return False

    # Delete uploaded file
    currentFile = uploadFilename(info)
    if os.path.exists(currentFile):
        os.remove(currentFile)

    # Delete all backups
    for backup in info["backups"]:
        path = backupPath(info, backup)
        if os.path.exists(path):
            os.remove(path)

    # Remove upload from each associated user
    for user in set(info["editors"] + info["viewers"]):
        noteUpload(user, creator, name, removed=True)

    # Remove even from the creator
    noteUpload(creator, creator, name, removed=True)

    # Delete the metadata
    return deleteInfo(dataKey(creator, name))


def readData(dataInfo):
    """
    Reads the data stored on disk for a particular upload, given the
    full metadata for the upload. Returns a string containing the entire
    file contents.

    Returns None (and flashes/prints a message) if there's an issue
    accessing the file.
    """
    filename = uploadFilename(dataInfo)

    if not os.path.exists(filename):
        msg = "File '{}' is missing for upload {}/{}".format(
            filename,
            dataInfo["creator"],
            dataInfo["name"],
        )
        flask.flash(msg)
        print(msg, file=sys.stderr)
        return None

    try:
        with open(filename, 'r') as fileInput:
            return fileInput.read()
    except Exception:
        msg = "Error accessing file '{}' for upload {}/{}".format(
            filename,
            dataInfo["creator"],
            dataInfo["name"],
        )
        flask.flash(msg)
        print(msg, file=sys.stderr)
        return None


def replaceData(dataInfo, dataOrUpload):
    """
    Replaces the data stored on disk for a particular upload with a new
    version (old versions are backed up). The provided object should
    either be a string (or bytes or unicode) or a
    `werkzeug.datastructures.FileStorage` object.

    Returns the name of the backup file created for the old data, or None
    if no old data existed.
    """
    # TODO: Don't backup large files, and/or have some control over
    # backups?

    # Check type of dataOrUpload (rest should be good since they come
    # from our stored data but it doesn't hurt to double-check)...
    typeCheckUploadInfo(
        creator=dataInfo["creator"],
        name=dataInfo["name"],
        format=dataInfo["format"],
        editors=dataInfo["editors"],
        viewers=dataInfo["viewers"],
        dataOrUpload=dataOrUpload
    )

    # Figure out filename to store data under
    filename = uploadFilename(dataInfo)

    # Make sure we've got directory structure in place
    ensureDirectory(os.path.dirname(filename))

    # Ensure we aren't overwriting anything (note that if an upload is
    # created and then deleted, re-creating it could otherwise cause an
    # overwrite):
    backup = makeWayFor(filename)

    # Write the data to disk
    if isinstance(dataOrUpload, werkzeug.datastructures.FileStorage):
        dataOrUpload.save(filename)
    else:
        # Handle bytes objects in Python 3
        if sys.version_info >= (3, 0) and isinstance(dataOrUpload, bytes):
            flags = 'wb'
        else:
            flags = 'w'

        # Handle unicode objects in Python 2
        if (
            sys.version_info < (3, 0)
        and isinstance(dataOrUpload, unicode) # noqa F821
        ):
            dataOrUpload = dataOrUpload.encode(ENCODING)

        with open(filename, flags) as outputFile:
            outputFile.write(dataOrUpload)

    # Note the backup and update the data info
    if backup is not None:
        backup = os.path.basename(backup)
        dataInfo["backups"].append(backup)
        setUploadInfo(dataInfo["creator"], dataInfo["name"], dataInfo)

    return backup


def addEditor(user, creator, dataName):
    """
    Adds the specified user as an editor for the data upload with the
    given name created by the given creator.

    Also updates their user data to list that permission.

    Does nothing and returns True if the user is already an editor for
    that data, but does remove them from the viewer list if they were on
    it (since editing permission is strictly more permissive than viewing
    permission).

    Returns True if it succeeds (including a non-update for an
    already-listed editor), or False if it fails (because the named
    upload doesn't exist).
    """
    info = getUploadInfo(creator, dataName)
    if info is None:
        return False

    if user in info["editors"]:
        return True

    info["editors"].append(user)

    # Either remove from viewers, or if not in viewers, update their
    # profile to show they have some kind of permission
    viewers = info["viewers"]
    if user in viewers:
        info["viewers"] = list(filter(lambda x: x != user, viewers))
    else:
        noteUpload(user, creator, dataName)

    setUploadInfo(creator, dataName, info)

    return True


def removeEditor(user, creator, dataName):
    """
    Removes the specified user from the editors list for the given
    upload data. Does nothing if they weren't on the list. Also updates
    their user profile to indicate they no longer have permissions for
    that view unless they somehow had view permissions set as well.

    Returns True if it succeeds, including if the editor didn't need to
    be removed, and False if it fails because the named upload does not
    exist.
    """
    info = getUploadInfo(creator, dataName)
    if info is None:
        return False

    editors = info["editors"]
    if user not in editors:
        return True

    info["editors"] = list(filter(lambda x: x != user, editors))

    if user not in info["viewers"]:
        noteUpload(user, creator, dataName, removed=True)

    setUploadInfo(creator, dataName, info)

    return True


def addViewer(user, creator, dataName):
    """
    Adds the specified user as a viewer for the data upload with the
    given name created by the given creator.

    Also updates their user data to list that permission.

    Does nothing if the user is already an editor or viewer for that
    data (editing permission is strictly more permissive than viewing
    permission).

    Returns True if it succeeds, including if the viewer didn't need to
    be added, and False if it fails because the named upload does not
    exist.
    """
    info = getUploadInfo(creator, dataName)
    if info is None:
        return False

    if user in info["viewers"] or user in info["editors"]:
        return True

    info["viewers"].append(user)

    # Note the permission in their profile
    noteUpload(user, creator, dataName)

    setUploadInfo(creator, dataName, info)

    return True


def removeViewer(user, creator, dataName):
    """
    Removes the specified user from the viewers list for the given
    upload data. Does nothing if they weren't on the list. Also updates
    their user profile to indicate they no longer have permissions for
    that view unless they somehow had edit permissions set as well.

    Returns True if it succeeds, including if the viewer didn't need to
    be removed, and False if it fails because the named upload does not
    exist.
    """
    info = getUploadInfo(creator, dataName)
    if info is None:
        return False

    viewers = info["viewers"]
    if user not in viewers:
        return True

    info["viewers"] = list(filter(lambda x: x != user, viewers))

    if user not in info["editors"]:
        noteUpload(user, creator, dataName, removed=True)

    setUploadInfo(creator, dataName, info)

    return True


#------------------------------#
# View data fetching functions #
#------------------------------#

_VIEWS_CHECKED = {}
"""
A cache of views that we've verified credentials for recently. We skip
checking view-creation permission (but not other kinds of permission) if
a view is listed here more recently than `VIEW_PERMISSION_CACHE_TIME`.
"""


def checkCachedPermission(viewInfo):
    """
    Checks whether the creator of a view has approval to create views of
    the data specified by the view's source type and source params (see
    `fetchViewData`), as listed in the permissions cache. Returns `True`
    or `False` if a value was cached, and `None` if there isn't a cached
    value, or if the cached value is too old (in that case, the cached
    value will be deleted as well). The cache time limit is determined by
    the `VIEW_PERMISSION_CACHE_TIME` config value, which can be set to
    `None` or zero to disable caching.
    """
    allow = _CONFIG.get("VIEW_PERMISSION_CACHE_TIME")
    # If caching is disabled, return None
    if allow is None or allow == 0:
        return None

    # Get value from cache
    cacheKey = (viewInfo["creator"],) + tuple(viewInfo["source"])
    valid, ts = _VIEWS_CHECKED.get(cacheKey, (None, None))
    # No result if there's no cache entry
    if ts is None:
        return None

    # Check freshness
    now = timeUtils.now()
    if now - ts < datetime.timedelta(seconds=allow):
        # Fresh, so we return cached value
        return valid
    else:
        # Stale, so we delete the entry
        del _VIEWS_CHECKED[cacheKey]
        return None


def cachePermission(viewInfo, valid):
    """
    Caches a permission check result (`valid` should be either `True` or
    `False`) for a given view.

    No entry is made if the `VIEW_PERMISSION_CACHE_TIME` config value is
    `None` or zero, since in that case caching is disabled.

    To avoid runaway cache growth, if the cache size has grown to more
    than `VIEW_PERMISSION_CACHE_SIZE_LIMIT` (default 1,000,000) the first
    `VIEW_PERMISSION_PRUNE` (default 100) entries will be deleted
    (depending on Python version, this means deleting 50 entries at
    random or the oldest 100).

    Note that a large `VIEW_PERMISSION_PRUNE` value will result in better
    amortized performance at the cost of worse worst-case performance.
    """
    allow = _CONFIG.get("VIEW_PERMISSION_CACHE_TIME")
    limit = _CONFIG.get("VIEW_PERMISSION_CACHE_SIZE_LIMIT", 1000000)
    prune = _CONFIG.get("VIEW_PERMISSION_PRUNE", 100)

    # Check whether caching is enabled at all:
    if allow is None or allow == 0:
        return

    # If we're over the cache key limit, prune some
    if len(_VIEWS_CHECKED) > limit:
        # Collect the first VIEW_PERMISSION_PRUNE entries
        counter = 0
        toDelete = []
        for key in _VIEWS_CHECKED:
            toDelete.append(key)
            counter += 1
            if counter >= prune:
                break

        for key in toDelete:
            del _VIEWS_CHECKED[key]

    key = (viewInfo["creator"],) + tuple(viewInfo["source"])
    _VIEWS_CHECKED[key] = (valid, timeUtils.now())


def checkViewPermissions(viewInfo):
    """
    Given a view info object, checks that the view creator has permission
    to create views of the data source, returning True if so and False if
    not.

    If `VIEW_PERMISSION_CACHE_TIME` is set in the configuration file,
    valid view permissions will be cached for that long, meaning that removing
    permission from a view may take at least that long to take effect.
    However, cached absent permissions are not rechecked, so that
    granting permission will take effect immediately. Note that this only
    affects who has permission to create views; if a view is deleted,
    access for everyone is shut off immediately.

    Returns `None` if the view's source value is wrong, and also prints &
    flashes an error message in that case.
    """
    creator = viewInfo["creator"]
    sourceType = viewInfo["source"][0]
    sourceParams = viewInfo["source"][1:]
    # Check cached permissions first. Note that we treat False and None
    # as the same, effectively ignoring cached False results, since we
    # expect those to be rare and we'd like fixes to be applied
    # immediately.
    if checkCachedPermission(viewInfo):
        return True

    nParams, checker, loader = SOURCE_TYPES.get(sourceType, (0, None, None))
    if checker is None:
        msg = "Invalid data source type: '{}'.".format(sourceType)
        flask.flash(msg)
        print(msg, file=sys.stderr)
        return None
    elif len(sourceParams) != nParams:
        msg = (
            "Wrong number of data source parameters (required {}): '{}'."
        ).format(nParams, sourceParams)
        flask.flash(msg)
        print(msg, file=sys.stderr)
        return None

    result = checker(creator, *sourceParams)
    cachePermission(viewInfo, result)
    return result


def fetchViewData(viewInfo):
    """
    Given a data source type (see `SOURCE_TYPES`) and further data source
    parameters specific to that source type, fetches the data, returning
    a list of dictionaries each representing one row of data (with the
    very first row omitted because it's used to determine the column
    names which are the keys of each dictionary).

    Note that you should always call `checkViewPermissions` first and
    refuse to fetch data if permissions aren't in order.

    Returns `None` if the data cannot be loaded, and also prints &
    flashes an error message in that case.
    """
    sourceType = viewInfo["source"][0]
    sourceParams = viewInfo["source"][1:]

    nParams, checker, loader = SOURCE_TYPES.get(sourceType, (0, None, None))
    if loader is None:
        msg = "Invalid data source type: '{}'.".format(sourceType)
        flask.flash(msg)
        print(msg, file=sys.stderr)
        return None
    elif len(sourceParams) != nParams:
        msg = (
            "Wrong number of data source parameters (required {}): '{}'."
        ).format(nParams, sourceParams)
        flask.flash(msg)
        print(msg, file=sys.stderr)
        return None

    return loader(*sourceParams)


def fetchUserView(viewInfo, user):
    """
    Fetches the user-visible info for a specific user viewing the
    specified view. This takes the form of a tuple containing a list of
    user rows followed by a list of header rows. The user rows and header
    rows each have one slot for each column, where the value of that
    slot is the value in a row matching the user's ID (possibly matching
    with a suffix, as specified by the view metadata). For header rows,
    the value in each slot is the value from the Nth header row, and
    these are included in the order they appear; if there are zero header
    rows (the default) the second element of the returned tuple is just
    an empty list. The first element of the tuple (the list of user rows)
    *always* has at least one entry.

    If there are no matching rows, this function returns `None` instead
    of a tuple; not even header information is returned. It also returns
    `None` in some other scenarios (like if the view is misconfigured or
    permissions aren't set properly) and in those cases it will flash &
    print a warning message.

    Note that the value in the index column of each header row must
    either be blank or start with '#'. This is to ensure that you don't
    accidentally leak user info via an invalid header row setup. If this
    condition is not met for one or more header row(s), a warning will be
    flashed/printed, and those header rows won't be included in the
    resulting header rows. It is possible for a header row to also be
    considered a matching row, although unless the username is blank or
    starts with '#', the above warning will always be triggered in that
    case.

    If the username is an empty string, no rows will be considered
    matches (even if a suffix is active) and an error message will be
    flashed and printed (the result will be `None`).
    """
    creator = viewInfo["creator"]
    viewName = viewInfo["name"]

    # Empty username is invalid
    if user == '':
        msg = "Empty username will not match anything."
        flask.flash(msg)
        print(msg, file=sys.stderr)
        return None

    permitted = checkViewPermissions(viewInfo)
    if not permitted:
        msg = (
            "View {}/{} is invalid because the creator has insufficient"
            " permissions."
        ).format(creator, viewName)
        flask.flash(msg)
        print(msg, file=sys.stderr)
        return None

    fullData = fetchViewData(viewInfo)
    if fullData is None:
        msg = "Could not fetch view data for {}/{}.".format(
            creator,
            viewName
        )
        flask.flash(msg)
        print(msg, file=sys.stderr)
        return None

    index = viewInfo["index"]
    headerRemaining = viewInfo["header"]
    headerRows = []
    matchAgainst = user + viewInfo["suffix"]
    matches = []
    for row in fullData:
        if index not in row:
            msg = (
                "Index column '{}' is not present in data for view {}/{}."
            ).format(index, creator, viewName)
            flask.flash(msg)
            print(msg, file=sys.stderr)
            return None

        indexValue = row[index]

        if headerRemaining > 0:
            if indexValue != "" and not indexValue.startswith('#'):
                msg = (
                    "Invalid index value '{}' in header row #{} for"
                    " view {}/{} (must be blank or start with '#')."
                ).format(
                    indexValue,
                    viewInfo['header'] - headerRemaining + 1,
                    creator,
                    viewName
                )
                flask.flash(msg)
                print(msg, file=sys.stderr)
                # This is a warning, not something that requires us to
                # abort
            else:
                headerRows.append(row)
            headerRemaining -= 1

        if indexValue == matchAgainst:
            matches.append(row)

    # No matches -> this user isn't part of this view
    if len(matches) == 0:
        return None

    return (matches, headerRows)


#-----------------------------------------#
# Format-specific data fetching functions #
#-----------------------------------------#

def asDictList(dataTable):
    """
    Given a list-of-lists-of-values structure representing a data table,
    returns a list-of-dictionaries representing the same data where the
    first row is used as the slot names for each dictionary.
    If the `dataTable` has 0 or 1 rows, an empty list will be returned.

    Handles rows of different lengths by assuming empty string values so
    that all row lengths match the length of the longest row.

    If multiple header values are identical, each row only retains the
    right-most value for that key.
    """
    result = []
    if len(dataTable) < 2:
        return []

    rowLen = max(len(row) for row in dataTable)

    header = dataTable[0]
    for row in dataTable[1:]:
        rowDict = {}
        for i in range(rowLen):
            if i < len(row):
                val = row[i]
            else:
                val = ''
            if i < len(header):
                key = header[i]
            else:
                key = ''

            rowDict[key] = val

        result.append(rowDict)

    return result


def checkGoogleSheetPermissions(viewCreator, sheetID, sheetName):
    """
    Checks whether the given view creator has permission to create views
    of the given sheet. The sheetName is ignored, since permission to
    create views applies to all sub-sheets, but it is listed as a
    parameter to match the parameters used for `fetchFromGoogleSheet`.

    Returns True if the view creator has permission and False if not.
    """
    return google.checkSheetViewPermissions(viewCreator, sheetID)


def fetchFromGoogleSheet(sheetID, sheetName):
    """
    Fetches raw data from a Google sheet, returning a list of
    dictionaries each representing one row of the sheet after the first
    row, which is used as the field names for the dictionaries. An empty
    list is returned if there is just one row or if there aren't any
    rows. If something goes wrong, this function will flash/print a
    warning message and return `None`.

    This function DOES NOT check view permissions; although the sheet
    must have been intentionally shared with the refraction account, the
    view creator may or may not have permission to create views of it
    (see `refraction.google.setup` for details on why we want to control
    that). Use `checkGoogleSheetPermissions` first to check permissions.

    See `refraction.google.readSheetValues` for details on how it works.
    """
    data = google.readSheetValues(sheetID, sheetName)
    if data is None:
        return None

    if len(data) == 0:
        return []

    return asDictList(data)


def hasPermissionToCreateViewOfUpload(
    viewCreator,
    uploadCreator,
    editors,
    viewers
):
    """
    Implements permission logic for whether a view creator has permission
    to create a view of an uploaded data item. Returns True if the
    specified view creator can create views of the upload with the given
    creator, editors list, and viewers list, or False if not. Unlike
    `checkUploadPermissions` this does not actually fetch the data info
    itself.
    """
    return (
        viewCreator == uploadCreator
     or viewCreator in editors
     or viewCreator in viewers
    )


def checkUploadPermissions(viewCreator, creator, dataName):
    """
    Checks whether the specified view creator has permission to create
    views of the upload data with the given creator & data name.

    Returns True if the view creator is the uploader, or if they're
    listed in the editors or viewers lists, and False otherwise,
    including in cases where the upload doesn't exist.
    """
    info = getUploadInfo(creator, dataName)
    if info is None:
        return False

    return hasPermissionToCreateViewOfUpload(
        viewCreator,
        info["creator"],
        info["editors"],
        info["viewers"],
    )


UPLOAD_FORMATS = ['CSV', 'TSV', 'JSON']
"""
The list of valid upload format strings.
"""


def fetchFromUploaded(creator, dataName):
    """
    Fetches raw data from an uploaded data object and parses it,
    returning a list of dictionaries each representing one row of the
    data after the first row, which is used as the field names for the
    dictionaries. If something goes wrong, this function will flash/print
    a warning message and return `None`.

    Note that this function does NOT check permissions; you should call
    `checkUploadPermissions` beforehand and respect that result.
    """
    info = getUploadInfo(creator, dataName)
    if info is None:
        msg = "Upload {}/{} does not exist.".format(creator, dataName)
        flask.flash(msg)
        print(msg, file=sys.stderr)
        return None

    format = info["format"]
    raw = readData(info)
    if format in ('CSV', 'TSV'):
        lines = raw.splitlines()
        reader = csv.DictReader(
            lines,
            dialect='excel-tab' if format == 'TSV' else 'excel'
        )
        return list(reader)
    elif format == "JSON":
        try:
            data = json.loads(raw)
        except Exception:
            tb = traceback.format_exc()
            msg = (
                "File for upload {}/{} is not valid JSON:\n{}"
            ).format(creator, dataName, tb)
            flask.flash(msg)
            print(msg, file=sys.stderr)
            return None

        if (
            not isinstance(data, list)
         or any(not isinstance(x, dict) for x in data)
        ):
            msg = (
                "Data object for upload {}/{} is in JSON format but is"
                " not a list of dictionaries."
            ).format(creator, dataName)
            flask.flash(msg)
            print(msg, file=sys.stderr)
            return None
        return info["data"]

    else:
        msg = "Unknown data format '{}' for data upload {}/{}.".format(
            format,
            creator,
            dataName
        )
        flask.flash(msg)
        print(msg, file=sys.stderr)
        return None


SOURCE_TYPES = {
    "upload": (2, checkUploadPermissions, fetchFromUploaded),
    "GoogleSheet": (2, checkGoogleSheetPermissions, fetchFromGoogleSheet),
}
"""
The mapping from recognized data source types to number-of-parameters,
permissions-checker, data-fetcher tuples for those types.
"""


#-----------#
# FileViews #
#-----------#

class FileView:
    """
    Abstract FileView class to organize decoding/encoding of files. Each
    `FileView` must define encode and decode class methods which are
    each others' inverse. The class name is used as part of the cache
    key. For read-only views, a exception (e.g., `NotImplementedError`)
    should be raised in the encode method.

    Note that the decode method may be given `None` as a parameter in
    situations where a file doesn't exist, and in most cases should
    simply pass that value through.
    """
    @staticmethod
    def encode(obj):
        """
        The encode function of a `FileView` must return a string (to be
        written to a file).
        """
        raise NotImplementedError("Don't use the base FileView class.")

    @staticmethod
    def decode(string):
        """
        The encode function of a `FileView` must accept a string, and if
        given a string produced by encode, should return an equivalent
        object.
        """
        raise NotImplementedError("Don't use the base FileView class.")


class AsIs(FileView):
    """
    A pass-through view that returns strings unaltered.
    """
    @staticmethod
    def encode(obj):
        """Returns the object it is given unaltered."""
        return obj

    @staticmethod
    def decode(string):
        """Returns the string it is given unaltered."""
        return string


class AsJSON(FileView):
    """
    A view that converts objects to JSON for file storage and back on
    access. It passes through None.
    """
    @staticmethod
    def encode(obj):
        """Returns the JSON encoding of the object."""
        return json.dumps(obj)

    @staticmethod
    def decode(string):
        """
        Returns a JSON object parsed from the string.
        Returns None if it gets None.
        """
        if string is None:
            return None
        return json.loads(string)


def buildView(name, encoder, decoder, passNone=True):
    """
    Function for building a view given a name, an encoding function, and
    a decoding function. Unless `passNone` is given as False, the
    decoder will be skipped if the decode argument is `None` and the
    `None` will pass through, in which case the decoder will *always*
    get a string as an argument.
    """
    class SyntheticView(FileView):
        """
        FileView class created using build_view.
        """
        @staticmethod
        def encode(obj):
            return encoder(obj)

        @staticmethod
        def decode(string):
            if passNone and string is None:
                return None
            return decoder(string)

    SyntheticView.__name__ = name
    SyntheticView.__doc__ = (
        "FileView that uses '{}' for encoding and '{}' for decoding."
    ).format(encoder.__name__, decoder.__name__)
    SyntheticView.encode.__doc__ = encoder.__doc__
    SyntheticView.decode.__doc__ = decoder.__doc__

    return SyntheticView


#------------------------#
# Read-only file caching #
#------------------------#

# Note: by using a threading.RLock and a global variable here, we are
# not process-safe, which is fine, because this is just a cache: each
# process in a multi-process environment can safely maintain its own
# cache which will waste a bit of memory but not lead to corruption. As
# a corollary, loadOrGetCached should be treated as read-only, otherwise
# one process might write to a file that's being read leading to
# excessively interesting behavior.

# TODO: We should probably have some kind of upper limit on the cache
# size, and maintain staleness so we can get rid of stale items...
_CACHE_LOCK = threading.RLock() # Make this reentrant just in case...
_CACHE = {}
"""
Cache of objects returned by view functions on cache keys.
"""


_FRESH_AT = {}
"""
Mapping from cache keys to tuples of seconds-since-epoch floats
representing the most recent time-span during which the file was found to
be unchanged. The first element of each tuple represents the earliest time
at which a freshness check succeeded with no subsequent failed checks,
and the second element represents the most recent time another successful
check was performed. Whenever a check is performed and succeeds, the
second element is updated, and whenever a check is performed and fails,
the value is set to None. When the value is None and a check succeeds,
both elements of the tuple are set to the current time.
"""


_MISSING = Exception
"""
What to return (wrapped in `AbortGeneration` if a file is found to be
missing during a freshness check. If the value is `Exception` (the
default) an exception will be raised instead.
"""


def checkFileIsChanged(cacheKey, ts):
    """
    Checks whether a file (specified using its cache key; see
    `cacheKeyFor` and `cacheKeyFilename`) has been modified more recently
    than the given timestamp. If the file doesn't exist, it returns
    `AbortGeneration` with the `_MISSING` value (unless `_MISSING` is
    left as the default of Exception, in which case it lets the
    exception bubble out).

    By default, checks that find the file was unchanged will be cached
    for 1 second, and repeated checks within that timeframe with
    more-recent timestamps will also return `False` even if the file is
    updated. The configuration value "ASSUME_FRESH" can be used to
    specify a different number of seconds, including 0 to turn this
    behavior off.

    As long as there is no cached value and the file exists, if the
    timestamp provided is `None`, this function returns `True`.
    """
    global _FRESH_AT
    now = time.time()
    cachedFresh = _FRESH_AT.get(cacheKey)
    if cachedFresh is not None:
        cachedFirst, cachedLast = cachedFresh
        if (
            ts is not None
        and ts >= cachedFirst
            # Note we don't check ts <= cachedLast here
        and now - cachedLast < _CONFIG.get("ASSUME_FRESH", 1)
        ):
            return False # we assume it has NOT changed

    filename = cacheKeyFilename(cacheKey)
    try:
        mtime = os.path.getmtime(filename)
    except OSError_or_FileNotFoundError:
        if _MISSING == Exception:
            raise
        else:
            return AbortGeneration(_MISSING)

    # File is changed if the mtime is after the given cache
    # timestamp, or if the timestamp is None
    result = ts is None or mtime >= ts

    # If file was changed, erase cached freshness
    if result:
        # If we find that a specific time was checked, and that time was
        # after the beginning of the current cached fresh period, we
        # erase the cached fresh period.
        if (
            ts is not None
        and (
                cachedFresh is not None
            and ts > cachedFirst
            )
        ):
            _FRESH_AT[cacheKey] = None

    # If file wasn't changed, extend cached freshness
    else:
        # In this branch ts is NOT None and it's strictly greater than mtime
        if cachedFresh is not None:
            # If an earlier-time-point was checked and the check
            # succeeded, we can extend the fresh-time-span backwards
            if ts < cachedFirst:
                cachedFirst = ts

            # If a later-time-point was checked and the check succeeded,
            # we can extend the fresh-time-span forwards
            if ts > cachedLast:
                cachedLast = ts

            # Update the fresh-time-span
            _FRESH_AT[cacheKey] = (cachedFirst, cachedLast)

        else: # If we didn't have cached freshness, initialize it
            _FRESH_AT[cacheKey] = (ts, ts)

    return result


def buildFileReader(view=AsJSON):
    """
    Builds a file reader function which returns the result of the given
    view on the file contents.
    """
    def readFile(cacheKey):
        """
        Reads a file and returns the result of calling a view's decode
        function on the file contents. Returns None if there's an error,
        and prints the error unless it's a FileNotFoundError.
        """
        # TODO: Check that the cache key's view matches the view
        # specified by this reader?
        filename = cacheKeyFilename(cacheKey)
        try:
            with open(filename, 'r') as fin:
                return view.decode(fin.read())
        except IOError_or_FileNotFoundError:
            return None
        except Exception:
            tb = traceback.format_exc()
            print(
                "[storage module] Exception viewing file:\n{}".format(tb),
                file=sys.stderr
            )
            return None

    return readFile


#--------------------#
# File I/O functions #
#--------------------#

def cacheKeyFor(target, view):
    """
    Builds a hybrid cache key value with a certain target and file view.
    """
    return target + '::' + view.__name__


def cacheKeyFilename(cacheKey):
    """
    Returns just the filename given a cache key.
    """
    filename = None
    for i in range(len(cacheKey) - 2, -1, -1):
        if cacheKey[i:i + 2] == '::':
            filename = cacheKey[:i]
            break
    if filename is None:
        raise ValueError("Value '{}' is not a cache key!".format(cacheKey))

    return filename


def loadOrGetCached(
    filename,
    view=AsIs
):
    """
    Reads the given file, returning its contents as a string. Doesn't
    actually do that most of the time. Instead, it will return a cached
    value. And instead of returning the contents of the file as a
    string, it returns the result of running the given view's decode
    function on the file's contents (after decoding those as a string).
    And actually, it caches the view result, not the file contents, to
    save time reapplying the view. The default view is `AsIs`, which
    loads the file contents as a string; `AsJSON` can be used to load
    JSON-encoded contents as a Python object.

    The `__name__` of the view class will be used to compute a cache key
    for that view; avoid view name collisions.

    If the file on disk is newer than the cache, re-reads and re-caches
    the file. If the config variable "ASSUME_FRESH" is set to a positive
    number, then the file time on disk isn't even checked if the most
    recent check was performed less than that many seconds ago.

    If the file is missing, an exception would normally be raised, but
    if the `_MISSING` value is set to something other than `Exception`, a
    deep copy of that value will be returned instead.

    Note: On a cache hit, a deep copy of the cached value is returned, so
    modifying that value should not affect what is stored in the cache.
    """

    # Figure out our view object (& cache key):
    if view is None:
        view = AsIs

    cacheKey = cacheKeyFor(filename, view)

    # Build functions for checking freshness and reading the file
    readFile = buildFileReader(view)

    return _genOrGetCached(
        _CACHE_LOCK,
        _CACHE,
        cacheKey,
        checkFileIsChanged,
        readFile
    )


#----------------------#
# Core caching routine #
#----------------------#

class AbortGeneration:
    """
    Class to signal that generation of a cached item should not proceed.
    Holds a default value to return instead.
    """
    def __init__(self, replacement):
        self.replacement = replacement


class NotInCache:
    """
    Placeholder for recognizing that a value is not in the cache (when
    e.g., None might be a valid cache value).
    """
    pass


def _genOrGetCached(
    lock,
    cache,
    cacheKey,
    checkDirty,
    resultGenerator
):
    """
    Common functionality that uses a reentrant lock and a cache
    dictionary to return a cached value if the cached value is fresh. The
    value from the cache is deep-copied before being returned, so that
    any modifications to the returned value shouldn't alter the cache.
    Parameters are:

        lock: Specifies the lock to use. Should be a threading.RLock.
        cache: The cache dictionary.
        cacheKey: String key for this cache item.
        checkDirty: Function which will be given the cacheKey and a
            timestamp and must return True if the cached value (created
            at that instant) is dirty (needs to be updated) and False
            otherwise. May also return an AbortGeneration instance with a
            default value inside to be returned directly. If there is no
            cached value, checkDirty will be given a timestamp of None.
        resultGenerator: Function to call to build a new result if the
            cached value is stale. This new result will be cached. It
            will be given the cacheKey as a parameter.
    """
    with lock:
        # Get cached value
        cacheTS, cached = cache.get(cacheKey, (None, NotInCache))
        safeCached = copy.deepcopy(cached)

    # Use the provided function to check if this cache key is dirty.
    # No point in storing the missing value we return since the dirty
    # check would presumably still come up True in the future.
    isDirty = checkDirty(cacheKey, cacheTS)
    if isinstance(isDirty, AbortGeneration):
        # check_fresh calls for an abort: return replacement value
        return isDirty.replacement
    elif not isDirty and cached != NotInCache:
        # Cache is fresh: return cached value
        return safeCached
    else:
        # Cache is stale

        # Get timestamp before we even start generating value:
        ts = time.time()

        # Generate result:
        result = resultGenerator(cacheKey)

        # Safely store new result value + timestamp in cache:
        with lock:
            cache[cacheKey] = (ts, result)
            # Don't allow outside code to mess with internals of
            # cached value (JSON results could be mutable):
            safeResult = copy.deepcopy(result)

        # Return fresh deep copy of cached value:
        return safeResult


#-----------------#
# Setup functions #
#-----------------#

_REDIS = None
"""
The connection to the REDIS server.
"""

_CONFIG = None
"""
The flask app's configuration object.
"""


def setup(config, key=None):
    """
    `setup` should be called once per process, ideally early in the life
    of the process, like right after importing the module. Calling some
    functions before `setup` will fail. A file named 'redis-pw.conf'
    should exist unless a key is given (should be a byte-string). If
    'redis-pw.conf' doesn't exist, it will be created.
    """
    global _REDIS, _CONFIG

    # Store config object
    _CONFIG = config

    # Ensure we have a data directory in our rundir
    ensureDirectory(config.get("DATA_DIR", '.'))

    # Set up google module
    google.setup(config)

    # Grab port from config
    port = config.get("STORAGE_PORT", 52317)

    # Redis configuration filenames
    rConfFile = "refraction-redis.conf"
    rUserFile = "refraction-redis-user.acl"
    rPortFile = "refraction-redis-port.conf"
    rPidFile = "refraction-redis.pid"
    rLogFile = "refraction-redis.log"

    # Check for redis config file
    if not os.path.exists(rConfFile):
        raise IOError_or_FileNotFoundError(
            "Unable to find Redis configuration file '{}'.".format(
                rConfFile
            )
        )

    # Check that conf file contains required stuff
    # TODO: More flexibility about these things?
    with open(rConfFile, 'r') as fin:
        rconf = fin.read()
        adir = 'aclfile "{}"'.format(rUserFile)
        if adir not in rconf:
            raise ValueError(
                (
                    "Redis configuration file '{}' is missing an ACL"
                    " file directive for the ACL file. It needs to use"
                    " '{}'."
                ).format(rConfFile, adir)
            )

        incl = "include {}".format(rPortFile)
        if incl not in rconf:
            raise ValueError(
                (
                    "Redis configuration file '{}' is missing an include"
                    " for the port file. It needs to use '{}'."
                ).format(rConfFile, incl)
            )

        pdecl = 'pidfile "{}"'.format(rPidFile)
        if pdecl not in rconf:
            raise ValueError(
                (
                    "Redis configuration file '{}' is missing the"
                    " correct PID file directive '{}'."
                ).format(rConfFile, pdecl)
            )

        ldecl = 'logfile "{}"'.format(rLogFile)
        if ldecl not in rconf:
            raise ValueError(
                (
                    "Redis configuration file '{}' is missing the"
                    " correct log file directive '{}'."
                ).format(rConfFile, ldecl)
            )

    # Get storage key:
    if key is None:
        try:
            if os.path.exists(rUserFile):
                with open(rUserFile, 'r') as fin:
                    key = fin.read().strip().split()[-1][1:]
            else:
                print(
                    "Creating new Redis user file '{}'.".format(
                        rUserFile
                    )
                )
                # b32encode here makes it more readable
                key = base64.b32encode(os.urandom(64)).decode("ascii")
                udecl = "user default on +@all ~* >{}".format(key)
                with open(rUserFile, 'w') as fout:
                    fout.write(udecl)
        except Exception:
            raise IOError_or_FileNotFoundError(
                "Unable to access user file '{}'.".format(rUserFile)
            )

    # Double-check port, or write port conf file
    if os.path.exists(rPortFile):
        with open(rPortFile, 'r') as fin:
            portStr = fin.read().strip().split()[1]
        try:
            portConf = int(portStr)
        except Exception:
            portConf = portStr

        if portConf != port:
            raise ValueError(
                (
                    "Port was specified as {}, but port conf file"
                    " already exists and says port should be {}."
                    " Delete the port conf file '{}' to re-write it."
                ).format(repr(port), repr(portConf), rPortFile)
            )
    else:
        # We need to write the port into the config file
        with open(rPortFile, 'w') as fout:
            fout.write("port " + str(port))

    _REDIS = redis.Redis(
        'localhost',
        port,
        password=key,
        decode_responses=True
    )
    # Attempt to connect; if that fails, attempt to start a new Redis
    # server and attempt to connect again. Abort if we couldn't start
    # the server.
    print("Attempting to connect to Redis server...")
    try:
        _REDIS.exists('test') # We just want to not trigger an error
        print("...connected successfully.")
    except redis.exceptions.ConnectionError: # nobody to connect to
        _REDIS = None
    except redis.exceptions.ResponseError: # bad password
        raise ValueError(
            "Your authentication key is not correct. Make sure"
            " you're not sharing the port you chose with another"
            " process!"
        )

    if _REDIS is None:
        print("...failed to connect...")
        if os.path.exists(rPidFile):
            print(
                (
                    "...a Redis PID file already exists at '{}', but we"
                    " can't connect. Please shut down the old Redis"
                    " server first, or clean up the PID file if it"
                    " crashed."
                ).format(rPidFile)
            )
            raise ValueError(
                "Aborting server startup due to existing PID file."
            )

        # Try to start a new redis server...
        print("...starting Redis...")
        try:
            subprocess.Popen(["redis-server", rConfFile])
        except OSError:
            # If running through e.g. Apache and this command fails, you
            # can try to start it manually, so we point that out
            if len(shlex.split(rConfFile)) > 1:
                rConfArg = "'" + rConfFile.replace("'", r"\'") + "'"
            else:
                rConfArg = rConfFile
            sys.stdout.write(
                (
                    "Note: Failed to start redis-server with an"
                    " OSError.\nYou could try to manually launch the"
                    " server by running:\nredis-server {}"
                ).format(rConfArg)
            )
            raise
        time.sleep(0.2) # try to connect pretty quickly
        print("...we hope Redis is up now...")

        if not os.path.exists(rPidFile):
            print(
                (
                    "...looks like Redis failed to launch; check '{}'..."
                ).format(rLogFile)
            )

        # We'll try a second time to connect
        _REDIS = redis.Redis(
            'localhost',
            port,
            password=key,
            decode_responses=True
        )
        print("Reattempting connection to Redis server...")
        try:
            _REDIS.exists('test') # We just want to not get an error
            print("...connected successfully.")
        except redis.exceptions.ConnectionError: # Not ready yet
            print("...not ready on first attempt...")
            _REDIS = None
        except redis.exceptions.ResponseError: # bad password
            raise ValueError(
                "Your authentication key is not correct. Make sure"
                " you're not sharing the port you chose with another"
                " process!"
            )

        # We'll make one final attempt
        if _REDIS is None:
            time.sleep(2) # Give it plenty of time

            # Check for PID file
            if not os.path.exists(rPidFile):
                print(
                    (
                        "...looks like Redis is still not running;"
                        " check '{}'..."
                    ).format(rLogFile)
                )

            # Set up connection object
            _REDIS = redis.Redis(
                'localhost',
                port,
                password=key,
                decode_responses=True
            )
            # Attempt to connect
            print(
                "Reattempting connection to Redis server (last"
                " chance)..."
            )
            try:
                _REDIS.exists('test') # We just want to not get an error
                print("...connected successfully.")
            except redis.exceptions.ResponseError: # bad password
                raise ValueError(
                    "Your authentication key is not correct. Make sure"
                    " you're not sharing the port you chose with another"
                    " process!"
                )
            # This time, we'll let a connection error bubble out

    # At this point, _REDIS is a working connection.


def cleanup():
    """
    Attempts to gracefully shut down the REDIS server. Does not try to
    clean up any files that may have been generated by `setup` or by the
    server, as these are typically used again when starting the server
    back up. After calling `cleanup`, REDIS functionality will no longer
    be available until `setup` is called again.

    Note that the server may not actually stop if there are conditions
    that prevent it from writing data to disk safely. The shutdown is
    initiated with `save` set to `True` to try to ensure data is saved;
    this means it may take some time for the server to shut down.

    Also removes the `_CONFIG` object, assuming a new one will be
    supplied when `setup` is called next. This means that most functions
    in this module will not work until `setup` is called.
    """
    global _REDIS, _CONFIG

    # Send shutdown message to server
    _REDIS.shutdown()

    # Remove connection variable
    _REDIS = None

    # Remove configuration global
    _CONFIG = None
