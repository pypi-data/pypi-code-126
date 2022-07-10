__version__ = '0.1.0'

from functools import wraps
import requests

from flask import request, abort, jsonify

from nsj_flask_auth.caching import Caching

from nsj_flask_auth.exceptions.unauthorized import Unauthorized
from nsj_flask_auth.exceptions.missing_auth_header import MissingAuthorizationHeader


class Auth:
    _cache = None

    def __init__(
        self, diretorio_uri: str = None,
        profile_uri: str = None,
        diretorio_api_key: str = None,
        api_key_header: str = 'X-API-Key',
        access_token_header: str = 'Authorization',
        user_required_permissions: list = [],
        app_required_permissions: list = [],
        caching_service=None
    ):
        self._diretorio_uri = diretorio_uri
        self._profile_uri = profile_uri
        self._diretorio_api_key = diretorio_api_key
        self._api_key_header = api_key_header
        self._access_token_header = access_token_header
        self._user_required_permissions = user_required_permissions
        self._app_required_permissions = app_required_permissions
        if caching_service:
            self._cache = Caching(caching_service)

    def verify_api_key(self, app_required_permissions: list = None):
        api_key = request.headers.get(self._api_key_header)

        if not api_key:
            raise MissingAuthorizationHeader(
                f'Missing {self._api_key_header} header')

        app_profile = self._get_app_profile(api_key)

        if app_profile['sistema']['nome']:
            return

        raise Unauthorized()

    def verify_access_token(self, user_required_permissions: list = None):
        access_token = request.headers.get(self._access_token_header)

        if not access_token:
            raise MissingAuthorizationHeader(
                f'Missing {self._access_token_header} header')

        user_profile = self._get_user_profile(access_token)

        if user_required_permissions:
            self.verify_user_permissions(
                user_required_permissions, user_profile)
            return

        if self._user_required_permissions:
            self.verify_user_permissions(
                self._user_required_permissions, user_profile)
            return

        if user_profile['email']:
            return

        raise Unauthorized()

    def verify_user_permissions(self, user_required_permissions: list, user_profile: dict):

        for organizacao in user_profile.get('organizacoes', []):
            if list(set(organizacao.get('permissoes', [])) & set(user_required_permissions)):
                return

        raise Unauthorized()

    def verify_api_key_or_access_token(self, app_required_permissions: list = None, user_required_permissions: list = None):

        try:
            self.verify_api_key(app_required_permissions)
            return
        except MissingAuthorizationHeader:
            pass

        try:
            self.verify_access_token(user_required_permissions)
            return
        except MissingAuthorizationHeader:
            pass

        raise Unauthorized()

    def requires_api_key(self, app_required_permissions: list = None):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                self.verify_api_key(app_required_permissions)
                return func(*args, **kwargs)
            return wrapper
        return decorator

    def requires_access_token(self, user_required_permissions: list = None):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                self.verify_access_token(user_required_permissions)
                return func(*args, **kwargs)
            return wrapper
        return decorator

    def requires_api_key_or_access_token(self, app_required_permissions: list = None, user_required_permissions: list = None):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    self.verify_api_key_or_access_token(
                        app_required_permissions, user_required_permissions)
                    return func(*args, **kwargs)
                except Unauthorized:
                    abort(jsonify({'error': 'Unauthorized'}), 401)
            return wrapper
        return decorator

    def _get_user_profile(self, access_token):

        if self._cache:
            user_profile = self._cache.get(access_token)
            if user_profile:
                return user_profile

        headers = {'Authorization': access_token}
        response = requests.get(self._profile_uri, headers=headers)

        if response.status_code != 200:
            raise Unauthorized()

        if self._cache:
            self._cache.set(access_token, response.json())

        return response.json()

    def _get_app_profile(self, api_key):

        if self._cache:
            app_profile = self._cache.get(api_key)
            if app_profile:
                return app_profile

        data = f"apikey={api_key}"

        headers = {
            "apikey": self._diretorio_api_key,
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.get(self._diretorio_uri,
                                data=data, headers=headers)

        if response.status_code != 200:
            raise Unauthorized()

        if self._cache:
            self._cache.set(api_key, response.json())

        return response.json()
