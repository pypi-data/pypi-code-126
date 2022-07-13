import json
import warnings
from datetime import date

import pkg_resources
from semver import VersionInfo


def schema():
    return json.load(pkg_resources.resource_stream(__name__, 'schema/.zenodo.json'))


def validate_zenodo_metadata(metadata):
    """
    Validate the zenodo metadata following the description from https://developers.zenodo.org/#representation
    Raise a ValueError if the metadata is not valid.
    Raise warnings for some important metadata.

    Parameters:
    ----------
    metadata: dict
    """
    if "version" in metadata and not VersionInfo.isvalid(metadata["version"].lstrip("v")):
        warnings.warn(f"Version {metadata['version']} does not follow the recommended format from semver.org.")

    if "upload_type" not in metadata:
        raise ValueError("upload_type is missing in the metadata.")
    elif metadata["upload_type"] not in [
        "publication",
        "poster",
        "presentation",
        "dataset",
        "image",
        "video",
        "software",
        "lesson",
        "physicalobject",
        "other",
    ]:
        raise ValueError(f"Invalid upload_type {metadata['upload_type']}")

    if metadata["upload_type"] == "publication":
        if "publication_type" not in metadata:
            raise ValueError("Missing publication_type")
        elif metadata["publication_type"] not in [
            "annotationcollection",
            "article",
            "book",
            "section",
            "conferencepaper",
            "datamanagementplan",
            "article",
            "patent",
            "preprint",
            "deliverable",
            "milestone",
            "proposal",
            "report",
            "softwaredocumentation",
            "taxonomictreatment",
            "technicalnote",
            "thesis",
            "workingpaper",
            "other",
        ]:
            raise ValueError(
                f"Invalid publication_type {metadata['publication_type']} " f"for upload_type {metadata['upload_type']}"
            )
    elif metadata["upload_type"] == "image":
        if "publication_type" not in metadata:
            raise ValueError("Missing publication_type")
        elif not metadata["publication_type"] in ["figure", "plot", "drawing", "diagram", "photo", "other"]:
            raise ValueError(
                f"Invalid publication_type {metadata['publication_type']} " f"for upload_type {metadata['upload_type']}"
            )

    if "publication_date" not in metadata:
        warnings.warn(f"Missing publication_date in the metadata, defaults to current date {date.today()}.")
    else:
        try:
            date.fromisoformat(metadata["publication_date"])
        except ValueError as exc:
            raise ValueError("Invalid publication_date, not isoformat") from exc

    if "title" not in metadata:
        raise ValueError("Missing title")

    if "creators" not in metadata:
        raise ValueError("Missing creators")
    elif not isinstance(metadata["creators"], list):
        raise ValueError("creators must be a list")
    else:
        for creator in metadata["creators"]:
            if "name" not in creator:
                raise ValueError(f"Missing name in creator {creator}")

    if "description" not in metadata:
        raise ValueError("Missing description")

    if "access_right" not in metadata:
        raise ValueError("Missing access_right")
    else:
        if metadata["access_right"] not in ["open", "closed", "embargoed", "restricted"]:
            raise ValueError(f"Invalid access_right {metadata['access_right']}")

    if "access_right" not in metadata:
        warnings.warn("Missing access_right in the metadata, defaults to open.")
    elif metadata["access_right"] in ["open", "embargoed"]:
        if "license" not in metadata:
            warnings.warn("Missing license in the metadata, defaults to CC-BY-4.0.")
    elif metadata["access_right"] == "restricted":
        if "embargo_date" not in metadata:
            raise ValueError("Missing embargo_date")
        else:
            try:
                date.fromisoformat(metadata["embargo_date"])
            except ValueError as exc:
                raise ValueError("Invalid embargo_date, not isoformat") from exc
    elif metadata["access_right"] == "restricted":
        if "access_conditions" not in metadata:
            raise ValueError("Missing access_conditions")

    return None
