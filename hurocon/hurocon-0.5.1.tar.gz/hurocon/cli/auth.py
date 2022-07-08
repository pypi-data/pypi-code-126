from click_didyoumean import DYMGroup

from ..implementation import iauth
from .cli_base import cli


@cli.group(cls=DYMGroup)
def auth():
    """ Router authentication """
    pass


@auth.command('login')
def auth_login():
    """ Safely configure all authentication related details for further interactions """
    iauth.auth_login_impl()


@auth.command('logout')
def auth_logout():
    """ Remove all authentication details """
    iauth.auth_logout_impl()


@auth.command('test')
def auth_test_connection():
    """ Test connection to router with current auth details """
    iauth.auth_test_connection_impl()
