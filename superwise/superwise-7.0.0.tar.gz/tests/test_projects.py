from datetime import datetime
from typing import List

import pytest
import requests
from google.cloud import storage
from google.oauth2 import service_account
from requests import Response

from superwise import Client
from superwise import Superwise
from superwise.models.project import Project


@pytest.fixture(scope="function")
def mock_get_token(monkeypatch):
    monkeypatch.setattr(
        Client,
        "get_token",
        lambda *args,
               **kwargs: "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjQ3ZDdmMDg2In0.eyJzdWIiOiI5YzNlZmUxZC03NGNlLTRlZTItYTMyOC1kMWZmNmQyMDAyM2YiLCJlbWFpbCI6InN3X2JhcmFrQHN1cGVyd2lzZS5haSIsInVzZXJNZXRhZGF0YSI6e30sInRlbmFudElkIjoiYmFyYWsiLCJyb2xlcyI6WyJWaWV3ZXIiXSwicGVybWlzc2lvbnMiOlsiZmUuc2VjdXJlLndyaXRlLnVzZXJBcGlUb2tlbnMiLCJmZS5zZWN1cmUuZGVsZXRlLnVzZXJBcGlUb2tlbnMiLCJmZS5zZWN1cmUucmVhZC51c2VyQXBpVG9rZW5zIl0sIm1ldGFkYXRhIjp7fSwiY3JlYXRlZEJ5VXNlcklkIjoiNDg5ZmM5Y2YtZDlhYy00MWMwLWJmM2ItN2VhNDUyNDY4ODEyIiwidHlwZSI6InVzZXJBcGlUb2tlbiIsInVzZXJJZCI6IjQ4OWZjOWNmLWQ5YWMtNDFjMC1iZjNiLTdlYTQ1MjQ2ODgxMiIsImlhdCI6MTYzNjY0ODIyMywiZXhwIjoxNjM2NzM0NjIzLCJpc3MiOiJmcm9udGVnZyJ9.qhEclIsSpfwXpCTFb8qhKpizRWtpQSnkE7VMsy9Et3guLcOcTiTVZ2wOJPmemtL3g3AStKH2jFSOEwQOoqnvgSR3dum9I_Ae3UwrFNRnM3EqOz7UsD0cJAd1AYy-69-67o5oX9A2U4MPZSA5Dr5Edbvn86-AsBJhADGDs5AyEyuGmlJTq0ACGAmoC8qZlxwnOsn9wIzTiQVU7085M73n5iJ26SNhsy4KNpU-8oR2lC1akDroHzL8aIr5dAWSWZz_cfcyWQyC1gqb4_ZAvG1GXiKwsGW2irFyfGoD9zrwMoMGuWXKCbXnHxIzuv8ImX_cRVPXq5xVBYUXwODr83Q3FA",
    )
    monkeypatch.setattr(Client, "get_service_account", lambda *args, **kwargs: {})


@pytest.fixture(scope="function")
def sw(mock_gcp_client):
    return Superwise(client_id="test", secret="test")


@pytest.fixture(scope="function")
def mock_gcp_client(monkeypatch):
    class GCSClient:
        def __init__(self, *args, **kwargs):
            self.name = "test"

        def bucket(self, bucket_name):
            return GCSClient()

        def blob(self, file_name):
            return GCSClient()

        def download_as_string(self):
            return "asdasdaas"

        def upload_from_string(self, data):
            return None

    monkeypatch.setattr(service_account.Credentials, "from_service_account_info", lambda *args, **kwargs: "")
    monkeypatch.setattr(storage, "Client", lambda *args, **kwargs: GCSClient())


@pytest.fixture(scope="function")
def mock_project_requests(monkeypatch):
    get_response = Response()
    get_response._content = b'{"id": 1, "name": "super cool project", "description": "here we have the most amazing project", "created_at": "2022-05-02T16:10:45.318683", "created_by": "me"}'
    get_response.status_code = 201

    delete_response = Response()
    delete_response._content = b'1'
    delete_response.status_code = 201

    monkeypatch.setattr(requests, "post", lambda *args, **kwargs: get_response)
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: get_response)
    monkeypatch.setattr(requests, "delete", lambda *args, **kwargs: delete_response)



@pytest.fixture(scope="function")
def mock_multi_project_requests(monkeypatch):
    get_response = Response()
    get_response._content = b'[{"id": 1, "name": "super cool project", "description": "here we have the most amazing project", "created_at": "2022-05-02T16:10:45.318683", "created_by": "me"},{"id": 1, "name": "super cool project", "description": "here we have the most amazing project", "created_at": "2022-05-02T16:10:45.318683", "created_by": "me"} ]'
    get_response.status_code = 201

    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: get_response)


def test_create_project(mock_project_requests, mock_get_token, sw):
    p = Project(name="super cool project", description="here we have the most amazing project")
    response = sw.project.create(p)
    assert response.id == 1 and response.name == p.name

def test_delete_project(mock_project_requests, mock_get_token, sw):
    project = Project(id=1, name="super cool project", description="here we have the most amazing project")
    res = sw.project.delete(project)
    assert res.status_code == 201
    assert res.json() in [project.id, f"{project.id}"]


def test_get_project_by_id(mock_project_requests, mock_get_token, sw):
    project = Project(id=1, name="super cool project", description="here we have the most amazing project")
    ret_project = sw.project.get_by_id(project.id)
    assert isinstance(ret_project, Project)
    assert project.name == ret_project.name


def test_get_project_by_name(mock_multi_project_requests, mock_get_token, sw):
    project = Project(id=1, name="super cool project", description="here we have the most amazing project")
    projects = sw.project.get_by_name(project.name)
    assert len(projects) == 2
