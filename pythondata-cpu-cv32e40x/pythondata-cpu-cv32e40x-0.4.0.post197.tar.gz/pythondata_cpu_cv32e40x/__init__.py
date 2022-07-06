import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.4.0.post197"
version_tuple = (0, 4, 0, 197)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post197")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post55"
data_version_tuple = (0, 4, 0, 55)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post55")
except ImportError:
    pass
data_git_hash = "e9dba5ebb74b031712b052302c7672ca1bd45ea4"
data_git_describe = "0.4.0-55-ge9dba5eb"
data_git_msg = """\
commit e9dba5ebb74b031712b052302c7672ca1bd45ea4
Merge: faa52330 09f3655f
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Wed Jul 6 11:09:29 2022 +0200

    Merge pull request #607 from silabs-oysteink/silabs-oysteink_zc-seq-ctrl
    
    Sequencer integration
    Self merging as agreed to enable merging to CV32E40X and continue on needed RVFI updates. Will revisit some feedback elements after the vacation season.

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
