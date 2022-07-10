import pytest
from _pytest.monkeypatch import MonkeyPatch
from fastapi import FastAPI
from starlette.testclient import TestClient

from authx_core import authxOpenAPI
from authx_core.errors import authxExpectedExceptions
from authx_core.utils import authxClearCaches


def get_app() -> FastAPI:
    app = FastAPI(debug=True)

    @app.get("/1")
    def endpoint_1() -> None:
        with authxExpectedExceptions(ValueError, detail=None):
            raise ValueError("debug message 1")

    @app.get("/2")
    def endpoint_2() -> None:
        with authxExpectedExceptions(ValueError, detail="prod message"):
            raise ValueError("debug message 2")

    authxOpenAPI(app)
    authxClearCaches()
    return app


@pytest.fixture
def debug_environment(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("API_DEBUG", "1")
    authxClearCaches()


@pytest.fixture
def prod_environment(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("API_DEBUG", "0")
    authxClearCaches()


@pytest.fixture
def debug_app(debug_environment: None) -> FastAPI:
    return get_app()


@pytest.fixture
def prod_app(prod_environment: None) -> FastAPI:
    return get_app()


def test_auth_app_1(debug_app: FastAPI) -> None:
    client = TestClient(debug_app)

    response = client.get(debug_app.url_path_for("endpoint_2"))
    assert response.json() == {"detail": "debug message 2"}, response.json()


def test_prod_app_1(prod_app: FastAPI) -> None:
    client = TestClient(prod_app)

    response = client.get(prod_app.url_path_for("endpoint_1"))
    assert response.json() == {"detail": "An error occurred"}, response.json()


def test_prod_app_2(prod_app: FastAPI) -> None:
    client = TestClient(prod_app)

    response = client.get(prod_app.url_path_for("endpoint_2"))
    assert response.json() == {"detail": "prod message"}, response.json()
