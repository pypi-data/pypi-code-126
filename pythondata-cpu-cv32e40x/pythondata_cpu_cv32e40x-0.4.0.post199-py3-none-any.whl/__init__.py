import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.4.0.post199"
version_tuple = (0, 4, 0, 199)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post199")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post57"
data_version_tuple = (0, 4, 0, 57)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post57")
except ImportError:
    pass
data_git_hash = "8c859523520d6d25d167bf2a98871f5ec39e0ffb"
data_git_describe = "0.4.0-57-g8c859523"
data_git_msg = """\
commit 8c859523520d6d25d167bf2a98871f5ec39e0ffb
Merge: e9dba5eb 8c8af41b
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Wed Jul 6 11:21:58 2022 +0200

    Merge pull request #609 from davideschiavone/fix608
    
    fix #608

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_cv32e40x."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_cv32e40x".format(f))
    return fn
