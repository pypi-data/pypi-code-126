# -*- coding: utf-8 -*-
"""

───│─────────────────────────────────────
───│────────▄▄───▄▄───▄▄───▄▄───────│────
───▌────────▒▒───▒▒───▒▒───▒▒───────▌────
───▌──────▄▀█▀█▀█▀█▀█▀█▀█▀█▀█▀▄─────▌────
───▌────▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄───▋────
▀███████████████████████████████████████▄─
──▀█████ flask_does_redis ████████████▀──
─────▀██████████████████████████████▀────
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

CONFIG

    REDIS_URL
    REDIS_HOST
    REDIS_PORT
    REDIS_DB
    REDIS_USERNAME
    REDIS_PASSWORD

HOW TO

    from flask_does_redis import RedisManager
    app = Flask(__name__)
    r = RedisManager(app)

    -OR-

    from flask_does_redis import RedisManager
    r = RedisManager()
    def create_app():
        app = Flask(__name__)
        r.init_app(app)

    -THEN-

    conn attribute is active connection
    r.conn.ping()

    pool attribute has connection pool
    instance = redis.Redis(connection_pool=r.pool)

    we also have convenience methods get(), set(), and delete()
    r.set("foo", "bar")
    r.get("foo")
    r.delete("foo")

    more advanced usage can be accomplished via conn

    d = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
    r.conn.mset(d)

"""

from redis import ConnectionPool
from redis import Redis


__version__ = "0.3.13+build.7"
__public_version__ = "0.3.13"
__author__ = "@jthop"


class RedisManager(object):

    CONN_CFG = ["url", "host", "port", "db", "username", "password"]

    def __init__(self, app=None):
        """Redis manager constructor.  Since we comply with app factory
        the constructor is put off until init_app()
        Args:
            app: Flask app beinging initialized from.
        """
        self.__version__ = __version__
        self.config = None
        self.name = None
        self.flask_app = None
        self.pool = None
        self.conn = None
        self.decode_responses = None
        self.auto_serialize = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """the init_app method called from the app_factory
        Args:
            app: Flask app beinging initialized from
        """

        if not hasattr(app, "extensions"):
            app.extensions = {}
        app.extensions["flask-does-redis"] = self
        self.flask_app = app
        self.name = self.flask_app.import_name

        self._set_default_config(app)
        self._parse_config(app)
        self._setup_pool()

        # as long as we have a pool, we can create a connection instance
        if self.pool:
            self.conn = Redis(connection_pool=self.pool)

    def _setup_pool(self):
        # use the url if available
        url = self.config.get("url")
        if url:
            self.pool = ConnectionPool.from_url(
                url, decode_responses=self.decode_responses
            )
            with self.flask_app.app_context():
                self.flask_app.logger.info(
                    f"Redis Manager pool instantiated with {url}"
                )

        # if no url is available, hopefully the remaining config has what is needed
        else:
            self.connection_config.pop("url")
            self.pool = ConnectionPool(
                **self.connection_config, decode_responses=self.decode_responses
            )
            with self.flask_app.app_context():
                self.flask_app.logger.info(
                    f"Redis Manager pool instantiated with {self.config}"
                )

    def _set_default_config(self, app):
        """Default config for our flask extension."""
        app.config.setdefault("REDIS_DECODE_RESPONSES", True)
        app.config.setdefault("REDIS_AUTO_SERIALIZE", True)

        app.config.setdefault("REDIS_HOST", "redis")
        app.config.setdefault("REDIS_URL", None)
        app.config.setdefault("REDIS_PORT", None)
        app.config.setdefault("REDIS_DB", None)
        app.config.setdefault("REDIS_USER", None)
        app.config.setdefault("REDIS_PASS", None)

    def _parse_config(self, app):
        """
        Fetch config in the REDIS_ namespace from the app.config dict.
        """

        cfg = app.config.get_namespace("REDIS_")
        clean = {k: v for k, v in cfg.items() if v is not None}
        self.config = clean
        self.decode_responses = clean.get("decode_responses")
        self.auto_serialize = clean.get("auto_serialize")

        self.connection_config = dict(
            url=clean.get("url"),
            host=clean.get("host"),
            port=clean.get("port"),
            db=clean.get("db"),
            username=clean.get("username"),
            password=clean.get("password"),
        )

    def get(self, k):
        """
        Simple convenience wrapper
        """
        if self.auto_serialize:
            pass

        return self.conn.get(k)

    def set(self, k, v, expire=None):
        """Wrapper for conn.set() but also allows
        you to supply an optional argument secs to set
        the key's expiration in with one line.
        """
        if self.auto_serialize:
            pass

        result = self.conn.set(k, v)
        if expire:
            return self.expire(k, secs)
        return result

    def delete(self, k):
        """
        Simple convenience wrapper
        """

        return self.conn.delete(k)

    def expire(self, k, secs):
        """
        Simple convenience wrapper
        """

        return self.conn.expire(k, secs)
