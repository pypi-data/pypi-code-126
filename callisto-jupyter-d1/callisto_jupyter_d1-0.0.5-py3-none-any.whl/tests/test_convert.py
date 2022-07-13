from io import StringIO
from typing import Dict

from fastapi.testclient import TestClient
from pytest_mock import MockFixture


def test_convert_rmd_to_ipynb(
    client: TestClient, readonly_token_headers: Dict[str, str],
) -> None:
    with open("jupyter_d1/tests/notebooks/worldpop.Rmd", "rb") as f1:
        response = client.post(
            "/convert/rmd_to_ipynb",
            files={"file": ("worldpop.Rmd", f1)},
            headers=readonly_token_headers,
        )
        with open("jupyter_d1/tests/notebooks/worldpop.ipynb", "rb") as f2:
            assert response.content == f2.read()

    assert (
        response.headers["content-disposition"]
        == 'attachment; filename="worldpop.ipynb"'
    )


def test_convert_rmd_with_R_to_ipynb(
    client: TestClient, readonly_token_headers: Dict[str, str],
) -> None:
    with open("jupyter_d1/tests/notebooks/rmd_example.Rmd", "rb") as f1:
        response = client.post(
            "/convert/rmd_to_ipynb",
            files={"file": ("rmd_example.Rmd", f1)},
            headers=readonly_token_headers,
        )
        with open("jupyter_d1/tests/notebooks/rmd_example.ipynb", "rb") as f2:
            print(response.content)
            assert response.content == f2.read()

    assert (
        response.headers["content-disposition"]
        == 'attachment; filename="rmd_example.ipynb"'
    )


def test_convert_rmd_to_ipynb_bogus_file(
    client: TestClient, readonly_token_headers: Dict[str, str], mocker: MockFixture
) -> None:
    mock_jupytext = mocker.patch(
        "jupyter_d1.routers.convert.jupytext"
    )
    mock_jupytext.side_effect = KeyError("it did not work")

    response = client.post(
        "/convert/rmd_to_ipynb",
        files={"file": (
            "meta_info.json",
            StringIO("%%%5not valid file\n````{{yurp}}\nprint(g)\n```")
        )},
        headers=readonly_token_headers,
    )
    assert response.status_code == 400    
    assert (
        response.json()["detail"] == "Failed to convert Rmd file to ipynb, do you have "
        "an R kernel installed and added to the kernelspecs?"
    )
