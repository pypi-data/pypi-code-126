from .handlers import RouteHandler
from jupyter_server.extension.application import ExtensionApp
from traitlets import Unicode, Bool, List
import pathlib
import os
import re


class ETCJupyterLabTelemetryCourseraApp(ExtensionApp):

    name = "etc_jupyterlab_telemetry_coursera"

    etc_url = Unicode("").tag(config=True)
    etc_bucket = Unicode("").tag(config=True)
    etc_path = Unicode("").tag(config=True)
    etc_env_path_segment_names = List([]).tag(config=True)
    etc_telemetry = Bool(None, allow_none=True).tag(config=True)
    etc_telemetry_path = Unicode("").tag(config=True)
    
    def initialize_settings(self):
        try:
            assert self.etc_url, "The c.ETCJupyterLabTelemetryCourseraApp.url configuration setting must be set."
            assert self.etc_bucket, "The c.ETCJupyterLabTelemetryCourseraApp.bucket configuration setting must be set."
        except Exception as e:
            self.log.error(str(e))
            raise e

    def initialize_handlers(self):
        try:
            self.handlers.extend([(r"/etc-jupyterlab-telemetry-coursera/(.*)", RouteHandler)])
        except Exception as e:
            self.log.error(str(e))
            raise e
