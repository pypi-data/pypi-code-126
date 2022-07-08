#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of the
# Flask-NameExtension Project (https://github.com/juniors90/Flask-NameExtension/).
# Copyright (c) 2022, Ferreira Juan David
# License: MIT
# Full Text: https://github.com/juniors90/Flask-NameExtension/blob/master/LICENSE

# =============================================================================
# DOCS
# =============================================================================

"""Flask-NameExtension.

Implementation of NameExtension in Flask.
"""


# =============================================================================
# IMPORTS
# =============================================================================
import warnings

from flask import Blueprint, Markup, current_app, url_for

# docstr-coverage:excused `no one is reading this anyways`
def raise_helper(message):  # pragma: no cover
    raise RuntimeError(message)

def some_filters():
    return "Hello World!!"

class NameExtension(object):
    """Base extension class for different of NameExtension versions.
    .. versionadded:: 0.0.1
    """

    fomantic_version = None
    static_folder = None

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Application factory."""

        # default settings
        app.config.setdefault("SOME_CONFIG_FOR_THIS_EXTENSION", False)

        if not hasattr(app, "extensions"):  # pragma: no cover
            app.extensions = {}
        
        app.extensions["extensionname"] = self
        
        blueprint = Blueprint(
            "extensionname",
            __name__,
            static_folder=f"static/{self.static_folder}",
            static_url_path=f"{app.static_url_path}",
            template_folder="templates",
        )

        app.register_blueprint(blueprint)

        app.jinja_env.globals["extensionname"] = self
        app.jinja_env.globals["some_filters"] = some_filters
        app.jinja_env.globals["warn"] = warnings.warn
        app.jinja_env.globals["raise"] = raise_helper
        app.jinja_env.add_extension("jinja2.ext.do")

        def hello(self, world):
            """The method example

            Parameters
            ----------
            world : str
                Some string.

            Return
            ------
            hello_world : str
                A string given by "Hello <world>".
            """
            hello_world = f"Hello {world}!!"
            return hello_world