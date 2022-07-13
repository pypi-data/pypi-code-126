import pathlib


def get_artifact_dir(hub):
    """
    function to get the full path to artifacts directory
    with the pkg_type included
    """
    pkg_type = "singlebin"
    if hub.OPT.heist.onedir:
        pkg_type = "onedir"
    artifacts_dir = pathlib.Path(hub.OPT.heist.artifacts_dir, pkg_type)
    if not artifacts_dir.is_dir():
        artifacts_dir.mkdir()
    return str(artifacts_dir)


def get_salt_path(hub, run_dir, target_os="linux"):
    """
    Return the full path to the salt binary.
    """
    binary_path = run_dir / "salt"
    if hub.OPT.heist.onedir:
        if target_os == "windows":
            binary_path = binary_path / "salt" / "salt.exe"
        else:
            binary_path = binary_path / "run" / "run"
    return binary_path
