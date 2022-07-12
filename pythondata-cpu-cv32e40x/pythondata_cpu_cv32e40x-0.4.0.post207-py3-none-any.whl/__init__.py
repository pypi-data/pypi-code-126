import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.4.0.post207"
version_tuple = (0, 4, 0, 207)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post207")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post65"
data_version_tuple = (0, 4, 0, 65)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post65")
except ImportError:
    pass
data_git_hash = "fa22670c7b0e83ffb4cc16aa72df020e37ed4078"
data_git_describe = "0.4.0-65-gfa22670c"
data_git_msg = """\
commit fa22670c7b0e83ffb4cc16aa72df020e37ed4078
Merge: f9193da0 c34a8fb4
Author: Henrik Fegran <henrik.fegran@silabs.com>
Date:   Tue Jul 12 09:34:27 2022 +0200

    Merge pull request #614 from silabs-hfegran/dev_hf_itrace_param
    
    Added parameter to disable itrace
    
    Merge OK'ed by @silabs-oysteink

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
