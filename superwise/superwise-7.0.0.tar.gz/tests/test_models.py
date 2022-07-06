from pprint import pprint

import pytest
import requests
from google.cloud import storage
from google.oauth2 import service_account
from requests import Response

from superwise import Client
from superwise import Superwise
from superwise.controller.exceptions import SuperwiseValidationException
from superwise.models.model import Model
from tests import print_results

model_id = None


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
def mock_create_model_inline(monkeypatch):
    original_post = requests.post
    model_mock = b'{"id":39,"name":"name","active_version_id":null,"active_version_ts":null,"description":"this is description","created_at":1650818206,"created_by":"d46edbbb-6f61-4508-8650-d05031bcd329","external_id":"39","time_units":["D","W"],"is_archived":false,"is_demo":false,"tags":[]}'

    post_model_response = Response()
    post_model_response.status_code = 201
    post_model_response._content = model_mock

    monkeypatch.setattr(requests, "post", lambda *args, **kwargs: post_model_response)
    yield None
    monkeypatch.setattr(requests, "post", original_post)


@pytest.fixture(scope="function")
def mock_create_model(monkeypatch):
    original_post = requests.post
    model_mock = b'{"id":40,"name":"this is test name","active_version_id":null,"active_version_ts":null,"description":"description","created_at":1650818210,"created_by":"d46edbbb-6f61-4508-8650-d05031bcd329","external_id":"40","time_units":["D","W"],"is_archived":false,"is_demo":false,"tags":[]}'

    post_model_response = Response()
    post_model_response.status_code = 201
    post_model_response._content = model_mock

    monkeypatch.setattr(requests, "post", lambda *args, **kwargs: post_model_response)
    yield None
    monkeypatch.setattr(requests, "post", original_post)


@pytest.fixture(scope="function")
def mock_get_model_list(monkeypatch):
    global model_id
    model_id = 15
    original_get = requests.get
    model_mock = b'[{"id":15,"external_id":"1078","name":"Chargeback prediction - task_id1078","description":"A multiclass classification model that decide whether to approve or reject a given transaction to avoid chargebacks","created_by":null,"active_version_id":14,"active_version_ts":"2021-07-26T17:31:39.416475","created_at":"2020-11-16T00:00:00","time_units":["D","W"],"is_archived":false,"tags":[]}]'
    get_model_response = Response()
    get_model_response.status_code = 201
    get_model_response._content = model_mock

    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: get_model_response)
    yield None
    monkeypatch.setattr(requests, "get", original_get)


@pytest.fixture(scope="function")
def mock_get_model(monkeypatch):
    global model_id
    model_id = 15
    original_get = requests.get
    model_mock = b'{"id":15,"name":"Chargeback prediction - task_id 1078","active_version_id":14,"active_version_ts":"2021-07-26T17:31:39.416475","description":"A multiclass classification model that decide whether to approve or reject a given transaction to avoid chargebacks","created_at":"2020-11-16T00:00:00","created_by":null,"external_id":"1078","time_units":["D","W"],"is_archived":false,"is_demo":false,"tags":[]}'
    get_model_response = Response()
    get_model_response.status_code = 201
    get_model_response._content = model_mock

    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: get_model_response)
    yield None
    monkeypatch.setattr(requests, "get", original_get)


@pytest.fixture(scope="function")
def mock_create_model_incomplete(monkeypatch):
    global model_id
    model_id = 15
    original_get = requests.post
    model_mock = b'{"detail":[{"loc":["body","name"],"msg":"none is not an allowed value","type":"type_error.none.not_allowed"}]}'
    get_model_response = Response()
    get_model_response.status_code = 422
    get_model_response._content = model_mock

    monkeypatch.setattr(requests, "post", lambda *args, **kwargs: get_model_response)
    yield None
    monkeypatch.setattr(requests, "post", original_get)


def test_create_model_inline(mock_create_model_inline, mock_get_token, sw):
    inline_model_test = sw.model.create(Model(name="name", description="this is description"))

    print_results("created model object 1", inline_model_test.get_properties())
    assert inline_model_test.name == "name"


def test_create_model(mock_create_model, mock_get_token, sw):
    model = Model()
    global model_id
    model.name = "this is test name"
    model.description = "description"
    model.ongoing_label = 12
    model.name = "this is test name"
    new_model_model = sw.model.create(model)
    print_results("created task object 2", new_model_model.get_properties())
    assert new_model_model.name == "this is test name"
    assert new_model_model.description == "description"
    task_id = new_model_model.id


def test_get_models_by_name(mock_get_model_list, mock_get_token, sw):
    global model_id
    print(model_id)
    models = sw.model.get_by_name("Chargeback prediction - task_id 1078")
    print(models)
    assert len(models) == 1
    model_id = models[0].id


def test_get_model(mock_get_model, mock_get_token, sw):
    global model_id
    print(model_id)
    model = sw.model.get_by_id(model_id)
    assert int(model.id) == model_id
    assert int(model.active_version_id) == 14


def test_create_incomplete_input(mock_create_model_incomplete, mock_get_token, sw):
    model = Model()
    ok = False
    try:
        ok = True
        model = sw.model.create(model)
    except SuperwiseValidationException as e:
        assert ok == True
        pprint(e)
    print(model.get_properties())

    ok2 = False
    try:
        new_inline = sw.model.create(Model(description="inline model description"))
    except SuperwiseValidationException as e:
        pprint(e)
        ok2 = True
    assert ok2 == True
