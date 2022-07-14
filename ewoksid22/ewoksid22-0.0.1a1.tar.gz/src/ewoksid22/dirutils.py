import os
import shutil
import socket

HOST_NAME = socket.gethostname()


def prepare_outdirs(
    outdirs, filename, include_proposal_outdir, proposal_subdir="ewoks_processed"
):
    """
    :param str filename: full path of the Nexus file
    :param dict outdirs:
    :param bool include_proposal_outdir:
    :returns dict:
    """
    if outdirs is None:
        outdirs = dict()
    if include_proposal_outdir:
        # dataset -> collection -> proposal (3 levels up)
        proposal_dir = os.path.dirname(os.path.dirname(os.path.dirname(filename)))
        proc_dir = os.path.join(proposal_dir, proposal_subdir)
        if "primary" in outdirs:
            outdirs["proposal"] = proc_dir
        else:
            outdirs["primary"] = proc_dir
    outdirs = {name: parse_outdir(dirname) for name, dirname in outdirs.items()}
    if "primary" not in outdirs:
        return dict()
    userhost, _ = outdirs["primary"]
    if userhost:
        raise ValueError("The primary output directory should be a local directory")
    return outdirs


def parse_outdir(dirname):
    """
    :param str dirname:
    :return 2-tuple:
    """
    err_msg = f"malformed directory name '{dirname}'"
    if dirname.count(":") > 1:
        raise ValueError(err_msg)
    parts = dirname.split(":")
    if len(parts) not in (1, 2):
        raise ValueError(err_msg)
    if len(parts) == 1:
        return None, dirname
    userhost, dirname = parts
    if userhost.endswith(HOST_NAME):
        return None, dirname
    return userhost, dirname


def copy_file(filename, outdirs):
    """Copy file from the primary output directory to the others.

    :param str filename:
    :param dict outdirs:
    """
    if not outdirs:
        return
    local_filename = primary_file(filename, outdirs)
    filename = os.path.basename(local_filename)
    for name, (userhost, dirname) in outdirs.items():
        if name == "primary":
            continue
        remote_filename = os.path.join(dirname, filename)
        if userhost:
            os.system(f'scp -q "{local_filename}" "{userhost}:{remote_filename}"')
        else:
            dirname = os.path.dirname(remote_filename)
            if dirname:
                os.makedirs(dirname, exist_ok=True)
            shutil.copyfile(local_filename, remote_filename)


def copy_file_to_primary(filename, outdirs):
    """Copy file to the primary output directory.

    :param str filename:
    :param dict outdirs:
    """
    shutil.copyfile(filename, primary_file(filename, outdirs))


def primary_file(filename, outdirs):
    """
    :param str filename:
    :param dict outdirs:
    """
    if not outdirs:
        return
    filename = os.path.basename(filename)
    return os.path.join(outdirs["primary"][1], filename)
