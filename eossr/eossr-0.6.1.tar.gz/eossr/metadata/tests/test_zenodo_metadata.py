import pytest

from eossr.metadata import zenodo


def test_zenodo_metadata():
    meta = {
        "title": "eOSSR unit test",
        "description": "eOSSR unit tests.",
        "version": "1.7.0",
        "creators": [{"affiliation": "The best affiliation", "name": "Rick"}],
        "access_right": "open",
        "upload_type": "software",
    }
    zenodo.validate_zenodo_metadata(meta)


@pytest.mark.xfail(raises=ValueError)
def test_zenodo_metadata_fail():
    meta = {
        "title": "eOSSR unit test",
        "creators": [{"affiliation": "The best affiliation", "name": "Rick"}],
        "access_right": "open",
        "upload_type": "image",
    }
    zenodo.validate_zenodo_metadata(meta)

    meta = {
        "title": "eOSSR unit test",
        "description": "eOSSR unit tests.",
        "creators": [{"affiliation": "The best affiliation"}],
        "access_right": "open",
        "upload_type": "image",
    }
    zenodo.validate_zenodo_metadata(meta)
