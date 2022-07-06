#!/usr/local/bin/python
# -*- coding: UTF-8 -*-
"""
Flask WSGI web app for displaying info from individual rows of a
spreadsheet to individual authenticated users (e.g., displaying grade
information to each student on a per-student basis).

To run the server, the current directory must contain `rfConfig.py` or
`rfConfig.py.example` which will be copied to create `rfConfig.py`. The
additional `secret` file will be created automatically using `os.urandom`
if necessary; see `rundir` in the package directory for an example.

Requirements include:

- `flask` web app framework
- `flask_cas` for CAS authentication
- `jinja2` for templates
- `redis` for storage/caching (you'll have to install the redis
    executable separately)
- `flask_talisman` and/or `flask_seasurf` for additional security
- `dateutil` for timezone handling
- `pyopenssl` for HTTPS encryption and content-security-policy in debug
    mode if `flask_talisman` is available (this helps spot errors earlier
    at the cost of having to click through a security warning from your
    browser about the self-signed certificate)
- `google-api-python-client`, `google-auth-httplib2`, and
    `google-auth-oauthlib` for access to Google API services if
    integration with Google Sheets is desired

First, an admin must set up a "view" which specifies where data is
retrieved from (see `storage.getViewInfo` for details). Currently, the
following data sources are supported:

- Reading from Google Sheets.
- Uploading a CSV or TSV file.

Any logged-in user (via CAS) whose ID appears in the specified column of
a created view can access that view and view info from the first matching
row in that column, but no other rows. If there are multiple rows that
contain a viewer's ID in the specified column, a warning will show up
both for that viewer and for all admins of that view.

Main routes:

/ (`routeIndex`):
    Checks for CAS authentication and redirects to login page or to
    `routeHome`.

/home (`routeHome`):
    Lists bookmarked & created views as well as data uploads, and allows
    creating new views and uploads.

/unbookmark/**$creator**/**$view** (`routeUnbookmark`):
    Removes a bookmark from the logged-in user's bookmarks and redirects
    back to the home view.

/createView (`routeCreateView`):
    Creates a new view, using POST data to specify the view properties
    including name, and with the effective user as the view creator.

/manage/**$creator**/**$view** (`routeManageView`):
    Shows a form for editing view details. Also used for creating a new
    view if the specified view does not yet exist. Requires login and
    being an admin or creator of the specified view. Anyone may create
    their own views, although there are restrictions in place to ensure
    that they have access to the data sources they use in those views.

/view/**$creator**/**$view** (`routeAutoView`):
    Redirects to `routeView` using the effective user as the viewer ID.
    This exists so you can give out non-viewer-specific links, while the
    viewer-specific nature of the full `routeView` allows view admins to
    easily see what their view looks like from the viewer's perspective.

/view/**$creator**/**$view**/**$username** (`routeView`):
    Main interface showing data from one row of a spreadsheet, as
    configured by the named view's creator (see above). Normally the
    username must match your CAS authentication, but any view admin can
    view the perspective of any user for that view.

/createUpload (`routeCreateUpload`):
    Creates a new upload, using POST data to specify the properties
    including name, and with the effective user as the upload creator.

/data/**$creator**/**$name** (`routeManageUpload`):
    Interface for viewing/updating uploaded CSV/TSV data to be used as a
    data source or views. Only visible to the creator and specific other
    users they list.

/upload/**$creator**/**$name** (`routeUpload`):
    Endpoint for uploading new CSV/TSV data; redirects to
    `routeManageUpload` once the upload is complete. Only usable by the
    creator & listed data editors.
"""

# Attempts at 2/3 dual compatibility:
from __future__ import print_function

__version__ = "0.1"

import sys

# IF we're not in pyhton3:
if sys.version_info[0] < 3:
    reload(sys) # noqa F821
    # Set explicit default encoding
    sys.setdefaultencoding('utf-8')
    # Rename raw_input
    input = raw_input # noqa F821
    ModuleNotFound_or_Import_Error = ImportError
else:
    ModuleNotFound_or_Import_Error = ModuleNotFoundError


# Main imports
import os, shutil, re # noqa E402

import flask # noqa E402
import flask_cas # noqa E402
import jinja2 # noqa E402
import markupsafe # noqa E402

from flask import json # noqa E402

from . import storage, timeUtils # noqa E402


#-------------#
# Setup setup #
#-------------#

class InitApp(flask.Flask):
    """
    A Flask app subclass which runs initialization functions right
    before app startup.
    """
    def __init__(self, *args, **kwargs):
        """
        Arguments are passed through to flask.Flask.__init__.
        """
        self.actions = []
        # Note: we don't use super() here since 2/3 compatibility is
        # too hard to figure out
        flask.Flask.__init__(self, *args, **kwargs)

    def init(self, action):
        """
        Registers an init action (a function which will be given the app
        object as its only argument). These functions will each be
        called, in order of registration, right before the app starts,
        withe the app_context active. Returns the action function
        provided, so that it can be used as a decorator, like so:

        ```py
        @app.init
        def setup_some_stuff(app):
            ...
        ```
        """
        self.actions.append(action)
        return action

    def setup(self):
        """
        Runs all registered initialization actions. If you're not running
        a debugging setup via the `run` method, you'll need to call this
        method yourself (e.g., in a .wsgi file).
        """
        with self.app_context():
            for action in self.actions:
                action(self)

    def run(self, *args, **kwargs):
        """
        Overridden run method runs our custom init actions with the app
        context first.
        """
        self.setup()
        # Note: we don't use super() here since 2/3 compatibility is
        # too hard to figure out
        flask.Flask.run(self, *args, **kwargs)


#-------#
# Setup #
#-------#

# Create our app object:
app = InitApp("refraction")


# Default configuration values if we really can't find a config file
DEFAULT_CONFIG = {
    "SUPPORT_EMAIL": 'username@example.com',
    "SUPPORT_LINK": '<a href="mailto:username@example.com">User Name</a>',
    "NO_DEBUG_SSL": False,
    "CAS_SERVER": 'https://login.example.com:443',
    "CAS_AFTER_LOGIN": 'dashboard',
    "CAS_LOGIN_ROUTE": '/module.php/casserver/cas.php/login',
    "CAS_LOGOUT_ROUTE": '/module.php/casserver/cas.php/logout',
    "CAS_AFTER_LOGOUT": 'https://example.com/potluck',
    "CAS_VALIDATE_ROUTE": '/module.php/casserver/serviceValidate.php',
    "ADMIN_FILE": 'refraction-admin.json',
    "TEMPLATE_DIRECTORY": 'templates',
    "STORAGE_PORT": 52317,
    "ASSUME_FRESH": 1,
    "GOOGLE_API_SERVICE_KEY_FILENAME": "credentials.json",
    "PERMISSIONS_SHEET_NAME": "refraction-permissions",
    "DOMAIN": "",
    "DATA_DIR": "uploads",
    "VIEW_PERMISSION_CACHE_TIME": 20,
    "VIEW_PERMISSION_CACHE_SIZE_LIMIT": 1000000,
    "VIEW_PERMISSION_PRUNE": 100,
}

# Loads configuration from file `rf_config.py`. If that file isn't
# present but `rf_config.py.example` is, copies the latter as the former
# first. Note that this CANNOT be run as an initialization pass, since
# the route definitions below require a working configuration.
try:
    sys.path.append('.')
    app.config.from_object('rf_config')
except Exception as e: # try copying the .example file?
    if os.path.exists('rf_config.py.example'):
        print("Creating new 'rf_config.py' from 'rf_config.py.example'.")
        shutil.copyfile('rf_config.py.example', 'rf_config.py')
        app.config.from_object('rf_config')
    else:
        print(
            "Neither 'rf_config.py' nor 'rf_config.py.example' is"
            " available, or there was an error in parsing them, so"
            " default configuration will be used."
        )
        print("CWD is:", os.getcwd())
        print("Error loading 'rf_config.py' was:", str(e))
        app.config.from_mapping(DEFAULT_CONFIG)
finally:
    sys.path.pop() # no longer need '.' on path...


@app.init
def setup_jinja_loader(app):
    """
    Set up templating with a custom loader that loads templates from the
    refraction package, and if a `TEMPLATE_DIRECTORY` is specified in
    the config file, templates from that directory will also be loaded.
    Templates in the directory override those in the package, so you can
    override default templates if you want to.
    """
    templateDir = app.config.get("TEMPLATE_DIRECTORY")
    if templateDir:
        app.jinja_loader = jinja2.ChoiceLoader([
            jinja2.FileSystemLoader(templateDir, followlinks=True),
            jinja2.PackageLoader("refraction", "templates")
        ])
    else:
        app.jinja_loader = jinja2.PackageLoader("refraction", "templates")


@app.init
def enable_CAS(app):
    """
    Enable authentication via a Central Authentication Server.
    """
    global cas
    cas = flask_cas.CAS(app)


@app.init
def create_secret_key(app):
    """
    Set secret key from secret file, or create a new secret key and
    write it into the secret file.
    """
    if os.path.exists("secret"):
        with open("secret", 'rb') as fin:
            app.secret_key = fin.read()
    else:
        print("Creating new secret key file 'secret'.")
        app.secret_key = os.urandom(16)
        with open("secret", 'wb') as fout:
            fout.write(app.secret_key)


@app.init
def initialize_storage_module(app):
    """
    Initialize file access and storage system.
    """
    storage.setup(app.config)


#----------------#
# Security setup #
#----------------#

NOAUTH = False
TEST_USERNAME = "test"
USE_TALISMAN = True
if __name__ == "__main__":
    # Print intro here...
    print("This is refraction version {}".format(__version__))

    print("WARNING: Running in debug mode WITHOUT AUTHENTICATION!")
    input("Press enter to continue in debug mode.")
    # Disable login_required
    flask_cas.login_required = lambda f: f
    # Set up username workaround
    NOAUTH = True

    # If OpenSSL is available, we can use talisman even if running in
    # local debugging mode; otherwise we need to disable talisman.
    try:
        import OpenSSL # noqa F401
    except ModuleNotFound_or_Import_Error:
        USE_TALISMAN = False

    # Config may disable talisman
    if app.config.get('NO_DEBUG_SSL'):
        USE_TALISMAN = False


@app.init
def enable_talisman(app):
    """
    Enable talisman forced-HTTPS and other security headers if
    `flask_talisman` is available and it won't interfere with debugging.
    """
    talisman_enabled = False
    if USE_TALISMAN:
        try:
            import flask_talisman
            # Content-security policy settings
            csp = {
                'default-src': "'self'",
                'script-src': "'self' 'report-sample'",
                'style-src': "'self'",
                'img-src': "'self' data:"
            }
            flask_talisman.Talisman(
                app,
                content_security_policy=csp,
                content_security_policy_nonce_in=[
                    'script-src',
                    'style-src'
                ]
            )
            talisman_enabled = True
        except ModuleNotFound_or_Import_Error:
            print(
                "Warning: module flask_talisman is not available;"
                " security headers will not be set."
            )

    if talisman_enabled:
        print("Talisman is enabled.")
    else:
        print("Talisman is NOT enabled.")
        # Add csp_nonce global dummy since flask_talisman didn't
        app.add_template_global(
            lambda: "-nonce-disabled-",
            name='csp_nonce'
        )


@app.init
def setup_seasurf(app):
    """
    Sets up `flask_seasurf` to combat cross-site request forgery, if
    that module is available.
    """
    try:
        import flask_seasurf
        csrf = flask_seasurf.SeaSurf(app) # noqa F841
    except ModuleNotFound_or_Import_Error:
        print(
            "Warning: module flask_seasurf is not available; CSRF"
            " protection will not be enabled."
        )
        # Add csrf_token global dummy since flask_seasurf isn't available
        app.add_template_global(lambda: "-disabled-", name='csrf_token')


#---------#
# Helpers #
#---------#

def augmentArguments(routeFunction):
    """
    A decorator that modifies a route function to supply `username`,
    `isAdmin`, `masqueradeAs`, and `effectiveUser` keyword arguments
    along with the other arguments the route receives. Must be applied
    before app.route.

    Because flask/werkzeug routing requires function signatures to be
    preserved, we do some dirty work with compile and eval... As a
    result, this function can only safely be used to decorate functions
    that don't have any keyword arguments. Furthermore, the 4 augmented
    arguments must be the last 4 arguments that the function accepts.
    """
    def withExtraArguments(*args, **kwargs):
        """
        A decorated route function which will be supplied with username,
        isAdmin, masqueradeAs, and effectiveUser parameters as keyword
        arguments after other arguments have been supplied.
        """
        # Get username
        if NOAUTH:
            username = TEST_USERNAME
        else:
            username = cas.username

        # Get admin info
        adminInfo = storage.getAdminInfo()
        if adminInfo is None:
            flask.flash("Error loading admin info!")
            adminInfo = {}

        # Check user privileges
        isAdmin, masqueradeAs = checkUserPrivileges(adminInfo, username)

        # Effective username
        effectiveUser = masqueradeAs or username

        # Update the kwargs
        kwargs["username"] = username
        kwargs["isAdmin"] = isAdmin
        kwargs["masqueradeAs"] = masqueradeAs
        kwargs["effectiveUser"] = effectiveUser

        # Call the decorated function w/ the extra parameters we've
        # deduced.
        return routeFunction(*args, **kwargs)

    # Grab info on original function signature
    fname = routeFunction.__name__
    nargs = routeFunction.__code__.co_argcount
    argnames = routeFunction.__code__.co_varnames[:nargs - 4]

    # Create a function with the same signature:
    code = """\
def {name}({args}):
    return withExtraArguments({args})
""".format(name=fname, args=', '.join(argnames))
    env = {"withExtraArguments": withExtraArguments}
    # 2/3 compatibility attempt...
    if sys.version_info[0] < 3:
        exec(code) in env, env
    else:
        exec(code, env, env) in env, env
    result = env[fname]

    # Preserve docstring
    result.__doc__ = routeFunction.__doc__

    # Return our synthetic function...
    return result


def goBack():
    """
    Returns a flask redirect aimed at either the page that the user came
    from, or the home page if that information isn't available.
    """
    if flask.request.referrer:
        # If we know where you came from, send you back there
        return flask.redirect(flask.request.referrer)
    else:
        # Otherwise back to the dashboard
        return flask.redirect(flask.url_for('routeHome'))


def errorResponse(username, cause):
    """
    Shortcut for displaying major errors to the users so that they can
    bug the support line instead of just getting a pure 404.
    """
    return flask.render_template(
        'error.j2',
        username=username,
        announcements="",
        support_link=app.config["SUPPORT_LINK"],
        error=cause
    )


def checkUserPrivileges(adminInfo, username):
    """
    Returns a pair containing a boolean indicating whether a user is an
    admin or not, and either None, or a string indicating the username
    that the given user is masquerading as.

    Requires admin info as returned by `storage.getAdminInfo`, plus the
    username of the user in question.
    """
    admins = adminInfo.get("admins", [])
    isAdmin = username in admins

    masqueradeAs = None
    # Only admins can possibly masquerade
    if isAdmin:
        masqueradeAs = adminInfo.get("MASQUERADE", {}).get(username)
        # You cannot masquerade as an admin
        if masqueradeAs in admins:
            flask.flash("Error: You cannot masquerade as another admin!")
            masqueradeAs = None
    elif adminInfo.get("MASQUERADE", {}).get(username):
        print(
            (
                "Warning: User '{}' cannot masquerade because they are"
              + "not an admin."
            ).format(username)
        )

    return (isAdmin, masqueradeAs)


def percentile(dataset, pct):
    """
    Computes the nth percentile of the dataset by a weighted average of
    the two items on either side of that fractional index within the
    dataset. pct must be a number between 0 and 100 (inclusive).

    Returns None when given an empty dataset, and always returns the
    singular item in the dataset when given a dataset of length 1.
    """
    fr = pct / 100.0
    if len(dataset) == 1:
        return dataset[0]
    elif len(dataset) == 0:
        return None
    srt = sorted(dataset)
    fridx = fr * (len(srt) - 1)
    idx = int(fridx)
    if idx == fridx:
        return srt[idx] # integer index -> no averaging
    leftover = fridx - idx
    first = srt[idx]
    second = srt[idx + 1] # legal index because we can't have hit the end
    return first * (1 - leftover) + second * leftover


#-----------------#
# Route functions #
#-----------------#

@app.route('/')
def routeIndex():
    """
    Checks authentication and redirects to login page or to home page.
    """
    if NOAUTH or cas.username:
        return flask.redirect(flask.url_for('routeHome'))
    else:
        return flask.redirect(flask.url_for('cas.login'))


@app.route('/home')
@flask_cas.login_required
@augmentArguments
def routeHome(username, isAdmin, masqueradeAs, effectiveUser):
    """
    Lists bookmarked views, created views, and data uploads. Allows
    creation of a new view or data upload, and bookmark management.

    Note that all arguments are supplied by `augmentArguments`.
    """
    userInfo = storage.getUserInfo(effectiveUser, create=True)

    # Render home template
    return flask.render_template(
        'home.j2',
        username=username,
        isAdmin=isAdmin,
        masqueradeAs=masqueradeAs,
        effectiveUser=effectiveUser,
        userInfo=userInfo
    )


@app.route('/unbookmark/<creator>/<view>')
@flask_cas.login_required
@augmentArguments
def routeUnbookmark(
    creator,
    view,
    # Augmented arguments
    username,
    isAdmin,
    masqueradeAs,
    effectiveUser
):
    """
    Removes a view from the effective user's bookmarks. Redirects back
    to the home view afterwards. Uses the URL to determine which
    bookmark is removed.
    """
    storage.removeBookmark(effectiveUser, creator, view)

    return flask.redirect(flask.url_for('routeHome'))


@app.route('/createView', methods=["POST"])
@flask_cas.login_required
@augmentArguments
def routeCreateView(
    # Augmented arguments
    username,
    isAdmin,
    masqueradeAs,
    effectiveUser
):
    fields = flask.request.form
    name = fields.get("name")
    if not name:
        flask.flash("You must specify a view name.")
        print(
            (
                "User {} attempted to create a view{} but didn't"
                " specify a name."
            ).format(
                username,
                ("as " + effectiveUser)
                    if username != effectiveUser
                    else ""
            ),
            file=sys.stderr
        )
        return goBack()

    source = fields.get("source").strip()
    if not source:
        flask.flash("You must specify a data source.")
        print(
            (
                "User {} attempted to create a view{} but didn't"
                " specify a data source."
            ).format(
                username,
                ("as " + effectiveUser)
                    if username != effectiveUser
                    else ""
            ),
            file=sys.stderr
        )
        return goBack()

    sourceParts = source.split() # 'not' check above means parts >= 1
    sourceType = sourceParts[0]
    if sourceType not in storage.SOURCE_TYPES:
        msg = "'{}' is not a valid data source type.".format(sourceType)
        flask.flash(msg)
        print(msg, file=sys.stderr)
        return goBack()

    sourceParams = sourceParts[1:]
    nParams = storage.SOURCE_TYPES[sourceType][0]
    if len(sourceParams) != nParams:
        msg = (
            "Wrong number of source parameters (needed {}, got {})"
        ).format(nParams, sourceParams)
        flask.flash(msg)
        print(msg, file=sys.stderr)
        return goBack()

    try:
        header = int(fields.get("header", 0))
    except ValueError:
        msg = (
            "Invalid header rows value (must be an integer): '{}'\nUsing"
            " 0 as a safe default."
        ).format(fields.get("header"))
        flask.flash(msg)
        print(msg, file=sys.stderr)
        header = 0

    # Get admins using split to create a list
    admins = fields.get("admins", '').strip()
    admins = [
        s.strip()
        for s in re.split("[ ,;]+", admins)
        if s.strip()
    ]

    succeeded = storage.createView(
        effectiveUser,
        name,
        source=sourceParts,
        admins=admins,
        contact=fields.get("contact", ''),
        index=fields.get("index", 'username'),
        suffix=fields.get("suffix"),
        header=header,
        template=fields.get("template", "")
    )

    if not succeeded:
        msg = (
            "Could create view '{}' because it already exists."
        ).format(name)
        flask.flash(msg)
        print(msg, file=sys.stderr)
        # We direct you to the manage route for that view
        return flask.redirect(
            flask.url_for(
                'routeManageView',
                creator=effectiveUser,
                view=name
            )
        )

    # Log access to the view, as the real user, not the effective user
    storage.logAccess(username, effectiveUser, name)

    return flask.redirect(
        flask.url_for(
            'routeManageView',
            creator=effectiveUser,
            view=name
        )
    )


@app.route('/manage/<creator>/<view>', methods=["GET", "POST"])
@flask_cas.login_required
@augmentArguments
def routeManageView(
    creator,
    view,
    # Augmented arguments
    username,
    isAdmin,
    masqueradeAs,
    effectiveUser
):
    """
    Displays view metadata and allows it to be updated. Only visible to
    admins of the view, plus the view creator. Also allows POST requests
    to update the view.
    """
    # Get view info for this view
    viewInfo = storage.getViewInfo(creator, view)

    # Check permissions
    if (
        effectiveUser not in viewInfo['admins']
    and effectiveUser != creator
    ):
        if isAdmin:
            flask.flash(
                "Note: you are not an admin for this view but as an app"
                " admin you can still manage it."
            )
        else:
            return errorResponse(
                effectiveUser,
                "{} is not allowed to manage view {}/{}.".format(
                    effectiveUser,
                    creator,
                    view
                )
            )

    # Make a note if you're managing someone else's view
    if creator != effectiveUser:
        flask.flash("You are managing {}'s view.".format(creator))

    # Log view access (not as effective user but as actual user)
    storage.logAccess(username, creator, view)

    # Handle incoming data if this is a POST request
    req = flask.request
    if req.method == "POST":
        fields = req.form

        # Update source using split to create a list (note that JS is
        # responsible for amalgamating source values from multiple
        # fields on the form side).
        newSource = fields.get("source", '').strip()
        # Note that an empty source list doesn't make sense which is why
        # if the source value is an empty string we can simply not update
        # the source at all.
        if newSource:
            sourceParts = newSource.split()
            viewInfo["source"] = sourceParts

            sourceType = sourceParts[0] # 'if' check makes this valid
            if sourceType not in storage.SOURCE_TYPES:
                msg = (
                    "'{}' is not a valid data source type."
                ).format(sourceType)
                flask.flash(msg)
                print(msg, file=sys.stderr)
                return goBack()

            sourceParams = sourceParts[1:]
            nParams = storage.SOURCE_TYPES[sourceType][0]
            if len(sourceParams) != nParams:
                msg = (
                    "Wrong number of source parameters (needed {}, got {})"
                ).format(nParams, sourceParams)
                flask.flash(msg)
                print(msg, file=sys.stderr)
                return goBack()

        # Update admins using split to create a list
        newAdmins = fields.get("admins", '').strip()
        newAdmins = [
            s.strip()
            for s in re.split("[ ,;]+", newAdmins)
            if s.strip()
        ]
        viewInfo["admins"] = newAdmins

        # Update simple fields that pass through as-is:
        for field in ["contact", "index", "suffix", "header", "template"]:
            newValue = fields.get(field)
            if newValue:
                viewInfo[field] = newValue

        # Save the new view info
        storage.setViewInfo(creator, view, viewInfo)

        # Make a copy if one was requested (other updates happen first)
        copy = fields.get("copy")
        copyAs = fields.get("copyAs")
        if copy and copyAs:
            succeeded = storage.createView(
                effectiveUser,
                copyAs,
                source=viewInfo["source"],
                contact=viewInfo["contact"],
                index=viewInfo["index"],
                suffix=viewInfo["suffix"],
                header=viewInfo["header"],
                template=viewInfo["template"]
            )
            if not succeeded:
                flask.flash(
                    (
                        "Cannot copy view {}/{} as {}/{}: that view"
                        " already exists."
                    ).format(creator, view, effectiveUser, copyAs)
                )

    # Whether method was POST or GET, we render the manager template
    return flask.render_template(
        'manageView.j2',
        creator=creator,
        viewName=view,
        username=username,
        isAdmin=isAdmin,
        masqueradeAs=masqueradeAs,
        effectiveUser=effectiveUser,
        viewInfo=viewInfo,
        supportLink=app.config["SUPPORT_LINK"]
    )


@app.route('/view/<creator>/<view>')
@flask_cas.login_required
@augmentArguments
def routeAutoView(
    creator,
    view,
    # Augmented arguments
    username,
    isAdmin,
    masqueradeAs,
    effectiveUser
):
    """
    Redirects to the full view route using the effective user's username
    as the viewer.
    """
    return flask.redirect(
        flask.url_for(
            'routeView',
            creator=creator,
            view=view,
            viewer=effectiveUser
        )
    )


@app.route('/view/<creator>/<view>/<viewer>')
@flask_cas.login_required
@augmentArguments
def routeView(
    creator,
    view,
    viewer,
    # Augmented arguments
    username,
    isAdmin,
    masqueradeAs,
    effectiveUser
):
    """
    Displays a view Using the specified template and showing the data
    accessible to a specific viewer. The viewer name must match the
    effective username, and if that user doesn't have data in that view,
    a generic page will be displayed indicating that. However, the view
    creator and view admins can see anyone's perspective, and app admins
    can see anyone's perspective on any view.
    """
    # Get view info for this view
    viewInfo = storage.getViewInfo(creator, view)

    # Check identity
    if effectiveUser != viewer:
        if (
            isAdmin
         or effectiveUser == creator
         or effectiveUser in viewInfo['admins']
        ):
            flask.flash(
                "You are viewing {viewer}'s perspective as an admin.".format(
                    viewer=viewer
                )
            )
        else:
            return flask.render_template(
                'wrongUsername.j2',
                creator=creator,
                viewName=view,
                viewer=viewer,
                username=username,
                isAdmin=isAdmin,
                masqueradeAs=masqueradeAs,
                effectiveUser=effectiveUser,
                viewInfo=viewInfo,
                supportLink=app.config["SUPPORT_LINK"]
            )

    # Get view data, which also checks permissions
    viewData = storage.fetchUserView(viewInfo, viewer)
    if viewData is None:
        return flask.render_template(
            'noDataView.j2',
            creator=creator,
            viewName=view,
            viewer=viewer,
            username=username,
            isAdmin=isAdmin,
            masqueradeAs=masqueradeAs,
            effectiveUser=effectiveUser,
            viewInfo=viewInfo,
            supportLink=app.config["SUPPORT_LINK"]
        )
    else:
        # Log view access (not as effective user but as actual user)
        storage.logAccess(username, creator, view)

        # Split view data into actual data + header rows
        userRows, headerRows = viewData

        # Fetch the view-specific template and render that...
        templateName = viewInfo["template"]
        if templateName:
            try:
                return flask.render_template(
                    templateName,
                    creator=creator,
                    viewName=view,
                    viewer=viewer,
                    userRows=userRows,
                    headerRows=headerRows,
                    username=username,
                    isAdmin=isAdmin,
                    masqueradeAs=masqueradeAs,
                    effectiveUser=effectiveUser,
                    viewInfo=viewInfo,
                    supportLink=app.config["SUPPORT_LINK"]
                )
            except Exception:
                return errorResponse(
                    effectiveUser,
                    (
                        "View {}/{} is misconfigured: unable to render view"
                        " template '{}'."
                    ).format(creator, view, templateName)
                )
        else:
            # if no custom template is specified, render using the
            # default template
            return flask.render_template(
                'view.j2',
                creator=creator,
                viewName=view,
                viewer=viewer,
                userRows=userRows,
                headerRows=headerRows,
                username=username,
                isAdmin=isAdmin,
                masqueradeAs=masqueradeAs,
                effectiveUser=effectiveUser,
                viewInfo=viewInfo,
                supportLink=app.config["SUPPORT_LINK"]
            )


@app.route('/createUpload', methods=["POST"])
@flask_cas.login_required
@augmentArguments
def routeCreateUpload(
    # Augmented arguments
    username,
    isAdmin,
    masqueradeAs,
    effectiveUser
):
    fields = flask.request.form

    # Ensure that a name was specified
    name = fields.get("name")
    if not name:
        flask.flash("You must specify an upload name.")
        print(
            (
                "User {} attempted to create an upload{} but didn't"
                " specify a name."
            ).format(
                username,
                ("as " + effectiveUser)
                    if username != effectiveUser
                    else ""
            ),
            file=sys.stderr
        )
        return goBack()

    # Ensure that there's a file that was uploaded
    files = flask.request.files
    if ('upload' not in files or files['upload'].filename == ''):
        flask.flash("You did not upload a data file.")
        return goBack()

    # Create the new upload object
    storage.createUpload(
        creator=effectiveUser,
        name=name,
        editors=[
            username.strip()
            for username in re.split("[ ,;]+", fields.get('editors', ''))
            if username.strip()
        ],
        viewers=[
            username.strip()
            for username in re.split("[ ,;]+", fields.get('viewers', ''))
            if username.strip()
        ],
        format=fields.get('format', 'CSV'),
        dataOrUpload=files['upload']
    )

    # Go to the management page for this upload
    return flask.redirect(
        flask.url_for(
            'routeManageUpload',
            creator=effectiveUser,
            name=name
        )
    )


@app.route('/data/<creator>/<name>', methods=["GET", "POST"])
@flask_cas.login_required
@augmentArguments
def routeManageUpload(
    creator,
    name,
    # Augmented arguments
    username,
    isAdmin,
    masqueradeAs,
    effectiveUser
):
    # Get data info
    dataInfo = storage.getUploadInfo(creator, name)

    # Get request object
    req = flask.request

    # Check permissions
    canEdit = (
        effectiveUser == creator
     or effectiveUser in dataInfo['editors']
    )
    canView = canEdit or effectiveUser in dataInfo['viewers']

    if not canEdit and not canView:
        if isAdmin:
            flask.flash(
                "Note: You are able to view this upload as an app admin."
            )
        else:
            return errorResponse(
                effectiveUser,
                "{} is not allowed to view upload {}/{}.".format(
                    effectiveUser,
                    creator,
                    name
                )
            )

    # If you're trying to update things, you need to be an editor, not
    # just a viewer
    if req.method == "POST" and not canEdit:
        if isAdmin:
            flask.flash(
                "Note: You are not an editor for this upload but as an"
                " app admin you can still manage it."
            )
        return errorResponse(
            effectiveUser,
            "{} is not allowed to edit upload {}/{}.".format(
                effectiveUser,
                creator,
                name
            )
        )

    # Make a note if you're managing someone else's data
    if creator != effectiveUser:
        if canEdit or isAdmin:
            flask.flash("You are managing {}'s upload.".format(creator))
        else:
            flask.flash("You are viewing {}'s upload.".format(creator))

    # Handle incoming data if this is a POST request
    if req.method == "POST":
        fields = req.form

        # Update editors using split and ignoring commas and semicolons:
        newEditors = fields.get("editors")
        # Note that None will leave the value unchanged, while any other
        # value (including an empty string) will change it.
        if newEditors is not None:
            newEditors = [
                s.strip()
                for s in re.split("[ ,;]+", newEditors)
                if s.strip()
            ]
            dataInfo["editors"] = newEditors

        # Update viewers likewise
        newViewers = fields.get("viewers")
        if newViewers is not None:
            newViewers = [
                s.strip()
                for s in re.split("[ ,;]+", newViewers)
                if s.strip()
            ]
            dataInfo["viewers"] = newViewers

        # Update format field directly
        newFormat = fields.get("format")
        # Note that here we treat None and empty string as the same,
        # since it doesn't make sense to not have a format. In both cases
        # we'll leave the old value unchanged.
        if not newFormat:
            newFormat = None
        else:
            dataInfo["format"] = newFormat

        # Save the new upload info
        storage.updateUpload(
            creator,
            name,
            format=newFormat,
            editors=newEditors,
            viewers=newViewers
        )

    # Read raw data to include in interface
    rawData = storage.readData(dataInfo)

    return flask.render_template(
        'manageUpload.j2',
        creator=creator,
        name=name,
        username=username,
        isAdmin=isAdmin,
        masqueradeAs=masqueradeAs,
        effectiveUser=effectiveUser,
        canEdit=canEdit,
        dataInfo=dataInfo,
        data=rawData,
        supportLink=app.config["SUPPORT_LINK"]
    )


@app.route('/upload/<creator>/<name>', methods=['POST'])
@flask_cas.login_required
@augmentArguments
def routeUpload(
    creator,
    name,
    # Augmented arguments
    username,
    isAdmin,
    masqueradeAs,
    effectiveUser
):
    # Get data info
    dataInfo = storage.getUploadInfo(creator, name)

    # Check permissions
    if (
        effectiveUser not in dataInfo['editors']
    and effectiveUser != creator
    ):
        if isAdmin:
            flask.flash(
                "Note: you are not an editor for this upload but as an"
                " app admin you were still permitted to replace it."
            )
        else:
            return errorResponse(
                effectiveUser,
                "{} is not allowed to upload/update {}/{}.".format(
                    effectiveUser,
                    creator,
                    name
                )
            )

    # Ensure that there's a file that was uploaded
    files = flask.request.files
    if ('upload' not in files or files['upload'].filename == ''):
        flask.flash("You did not upload a file.")
        return goBack()
    else:
        # Save the file
        # TODO: Track saved versions and include restore mechanism...
        #backup = storage.replaceData(dataInfo, files['upload'])
        storage.replaceData(dataInfo, files['upload'])

        # Go back to where you came from
        return goBack()


#---------------#
# Jinja support #
#---------------#

# Turn builtin sorted into a template filter...
sorted = app.template_filter()(sorted)

# Time values to make code below clearer
# Does not correctly handle leap time over long periods of time, but we
# are okay with fuzzyTime being slightly inaccurate in those cases.
ONE_MINUTE = 60
ONE_HOUR = ONE_MINUTE * 60
ONE_DAY = ONE_HOUR * 24
ONE_WEEK = ONE_DAY * 7
ONE_YEAR = ONE_DAY * 365.25


@app.template_filter()
def fuzzyTime(seconds):
    """
    Takes a number of seconds and returns a fuzzy time value that shifts
    units (up to years) depending on how many seconds there are. Ignores
    the sign of the value.
    """
    if seconds < 0:
        seconds = -seconds

    years = seconds / ONE_YEAR
    weeks = seconds / ONE_WEEK
    seconds %= ONE_WEEK
    days = seconds / ONE_DAY
    seconds %= ONE_DAY
    hours = seconds / ONE_HOUR
    seconds %= ONE_HOUR
    minutes = seconds / ONE_MINUTE
    seconds %= ONE_MINUTE
    if int(years) > 1:
        if years % 1 > 0.8:
            return "almost {} years".format(int(years) + 1)
        else:
            return "{} years".format(int(years))
    elif int(weeks) > 1:
        if weeks % 1 > 0.75:
            return "almost {} weeks".format(int(weeks) + 1)
        else:
            return "{} weeks".format(int(weeks))
    elif int(weeks) == 1:
        return "{} days".format(7 + int(days))
    elif int(days) > 1:
        if days % 1 > 0.75:
            return "almost {} days".format(int(days) + 1)
        else:
            return "{} days".format(int(days))
    elif int(days) == 1:
        return "{} hours".format(24 + int(hours))
    elif hours > 4:
        if hours % 1 > 0.75:
            return "almost {} hours".format(int(hours) + 1)
        else:
            return "{} hours".format(int(hours))
    elif int(hours) > 0:
        return "{}h {}m".format(int(hours), int(minutes))
    elif minutes > 30:
        return "{} minutes".format(int(minutes))
    else:
        return "{}m {}s".format(int(minutes), int(seconds))


# Add `timeUtils.toDatetime` as a template filter
timeUtils.toDatetime = app.template_filter()(timeUtils.toDatetime)


@app.template_filter()
def secondsUntil(timeData):
    """
    A filter to convert a time value (expressed as a time string, a
    floating-point timestamp, or a `datetime.datetime` object) into a
    number of seconds difference from the present time, with positive
    numbers indicating times in the future and negative numbers
    indicating times in the past.
    """
    dt = timeUtils.toDatetime(timeData)
    diff = dt - timeUtils.now()
    return diff.total_seconds()


@app.template_filter()
def until(timeData):
    """
    Converts a time string, timestamp, or `datetime` object into a
    string describing how far "from now" or "ago" that time is. Uses
    `fuzzyTime` to be broadly descriptive while remaining concise.
    """
    seconds = secondsUntil(timeData)
    fuzzy = fuzzyTime(seconds)
    if seconds <= 0:
        return fuzzy + " ago"
    else:
        return fuzzy + " from now"


@app.template_filter()
def timestamp(value):
    """
    A filter to display a time string.
    """
    dt = timeUtils.timeFromTimeString(value)
    return timeUtils.describeTime(dt)


@app.template_filter()
def seconds(timedelta):
    """
    Converts a timedelta to a floating-point number of seconds.
    """
    return timedelta.total_seconds()


@app.template_filter()
def integer(value):
    """
    A filter to display a number as an integer via rounding
    (non-numerical values are unchanged).
    """
    if isinstance(value, (float, int)):
        return str(round(value))
    else:
        return str(value)


app.add_template_global(min, name='min')
app.add_template_global(max, name='max')
app.add_template_global(round, name='round')
app.add_template_global(sum, name='sum')

# Time filters from potluck
timeUtils.describeTime = app.template_filter()(timeUtils.describeTime)


@app.template_filter()
def a_an(h):
    """
    Returns the string 'a' or 'an' where the use of 'a/an' depends on the
    first letter of the name of the first digit of the given number, or
    the first letter of the given string.

    Can't handle everything because it doesn't know phonetics (e.g., 'a
    hour' not 'an hour' because 'h' is not a vowel).

    Returns 'a' if the string is empty.
    """
    letters = str(h)
    if len(letters) == 0:
        return 'a'
    fd = letters[0]
    if fd in "18aeiou":
        return 'an'
    else:
        return 'a'


# Characters that need replacing to avoid breaking strings in JS script
# tags
_JS_ESCAPES = [ # all characters with ord() < 32
    chr(z) for z in range(32)
] + [
    '\\',
    "'",
    '"',
    '>',
    '<',
    '&',
    '=',
    '-',
    ';',
    u'\u2028', # LINE_SEPARATOR
    u'\u2029', # PARAGRAPH_SEPARATOR
]


@app.template_filter()
def escapejs(value):
    """
    Modified from:

    https://stackoverflow.com/questions/12339806/escape-strings-for-javascript-using-jinja2

    Escapes string values so that they can appear inside of quotes in a
    &lt;script&gt; tag and they won't end the quotes or cause any other
    trouble.
    """
    retval = []
    for char in value:
        if char in _JS_ESCAPES:
            retval.append(r'\u{:04X}'.format(ord(char)))
        else:
            retval.append(char)

    return markupsafe.Markup(u"".join(retval))


#-----------#
# Main code #
#-----------#

if __name__ == "__main__":
    if USE_TALISMAN:
        # Run with an ad-hoc SSL context since OpenSSL is available and
        # SSL was not disabled in debug mode
        print("Running with self-signed SSL.")
        app.run('localhost', 8787, debug=False, ssl_context='adhoc')
    else:
        # Run without an SSL context (No OpenSSL)
        print("Running without SSL.")
        app.run('localhost', 8787, debug=False)
        # Note: can't enable debugging because it doesn't set __package__
        # when restarting and so relative imports break in 3.x
