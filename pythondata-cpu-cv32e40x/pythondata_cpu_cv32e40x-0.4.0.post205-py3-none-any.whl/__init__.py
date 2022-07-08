import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.4.0.post205"
version_tuple = (0, 4, 0, 205)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post205")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post63"
data_version_tuple = (0, 4, 0, 63)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post63")
except ImportError:
    pass
data_git_hash = "f9193da05ca3faed7bc4472ff1c5a65a737d7a0e"
data_git_describe = "0.4.0-63-gf9193da0"
data_git_msg = """\
commit f9193da05ca3faed7bc4472ff1c5a65a737d7a0e
Merge: be24e5c3 79160b48
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Fri Jul 8 09:54:17 2022 +0200

    Merge pull request #613 from silabs-oysteink/silabs-oysteink_rvfi-zc
    
    Self merging due to vacation season. Should be reviewed later.

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
