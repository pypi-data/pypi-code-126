import importlib.metadata


def test_version():
    assert importlib.metadata.version("groll") == "0.0.3"
