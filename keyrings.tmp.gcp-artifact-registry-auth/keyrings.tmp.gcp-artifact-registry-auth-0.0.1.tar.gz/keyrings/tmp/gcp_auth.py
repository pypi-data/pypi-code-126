from keyring import backend
from keyring import credentials
from urllib.parse import urlparse

from google.auth import default
from google.auth.transport import requests
from google.auth.exceptions import DefaultCredentialsError, RefreshError

import json
import logging
import subprocess

class GCPPythonAuth(backend.KeyringBackend):
  priority = 9

  def get_password(self, service, username):
    url = urlparse(service)
    hostname = service if url.hostname is None else url.hostname

    if hostname is None or not hostname.endswith(".pkg.dev"):
      return

    try:
      creds, _ = default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
      creds.refresh(requests.Request())
      return creds.token
    except (DefaultCredentialsError, RefreshError) as exception:
      logging.warning(f"Failed to retrieve Application Default Credentials: {exception}")

    try:
      return self.get_gcloud_credential()
    except DefaultCredentialsError as exception:
      logging.warning(f"Failed to retrieve credentials from gcloud: {exception}")

    logging.warning("GCP Artifact Registry PyPI Keyring: No credentials could be found.")
    raise Exception("Failed to find credentials, Please run: `gcloud auth application-default login or export GOOGLE_APPLICATION_CREDENTIALS=<path/to/service/account/key>`")

  def set_password(self, service, username, password):
    raise NotImplementedError()

  def delete_password(self, service, username):
    raise NotImplementedError()

  def get_credential(self, service, username):
    password = self.get_password(service, username)
    if password is not None:
      return credentials.SimpleCredential("oauth2accesstoken", password)
    return None

  @staticmethod
  def get_gcloud_credential():
    try:
      logging.warning("Trying to retrieve credentials from gcloud...")
      command = subprocess.run(['gcloud', 'config', 'config-helper', '--format=json(credential)'], check=True, stdout=subprocess.PIPE, universal_newlines=True)
    except Exception as exception:
      raise DefaultCredentialsError(f"gcloud command exited with status: {exception}") from exception

    credential = json.loads(command.stdout).get("credential")

    if credential is None:
      raise DefaultCredentialsError("No credential returned from gcloud")

    if "access_token" not in credential or "token_expiry" not in credential:
      raise DefaultCredentialsError("Malformed response from gcloud")

    return credential.get("access_token")
