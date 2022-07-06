"""

"""
import platform
import os
import glob
import sys
import errno
import json
# /users/me/Conductor/ciohoudini
PKG_DIR = os.path.dirname(os.path.abspath(__file__))

# /users/me/Conductor/
CIO_DIR = os.path.dirname(PKG_DIR)

# ciohoudini
PKGNAME = os.path.basename(PKG_DIR)

PLATFORM = sys.platform
with open(os.path.join(PKG_DIR, 'VERSION')) as version_file:
    VERSION = version_file.read().strip()

# In development, we want to keep the HDA in the dev location (under env var CIO).
# In production, we want to move the HDA to the user's Conductor directory.
# The python package is always pip installed in the user's Conductor directory.
if os.environ.get("CIO_FEATURE_DEV"):
    houdini_path = os.path.join(os.environ.get("CIO"), "ciohoudini","ciohoudini")
else:
    houdini_path = "$CIODIR/ciohoudini"

PACKAGE_FILE_CONTENT = {
    "env": [
        {
            "CIODIR": CIO_DIR
        },
         {
            "var": "HOUDINI_PATH",
            "value": [
               houdini_path
            ]
        },
        {
            "PYTHONPATH": {
                "method": "prepend",
                "value": [
                    "$CIODIR"
                ]
            }
        }
    ]
}


def main():
    if not PLATFORM in ["darwin", "win32", "linux"]:
        sys.stderr.write("Unsupported platform: {}".format(PLATFORM))
        sys.exit(1)

    for pkg_file in get_package_files():
        try:
            ensure_directory(os.path.dirname(pkg_file))
        except BaseException:
            pass

        with open(pkg_file, 'w') as f:
            json.dump(PACKAGE_FILE_CONTENT, f, indent=4)
    
        sys.stdout.write("Added  Conductor Houdini package file: {}".format(pkg_file))


def get_package_files():

    if PLATFORM == "darwin":
        pattern = "~/Library/Preferences/houdini/[0-9][0-9]*"
    elif PLATFORM == "linux":
        pattern = "~/houdini[0-9][0-9]*"
    else:  # windows
        pattern = "~/houdini[0-9][0-9]*"

    return [os.path.join(p, "packages", "conductor.json") for p in glob.glob(os.path.expanduser(pattern))]


def ensure_directory(directory):
    try:
        os.makedirs(directory)
    except OSError as ex:
        if ex.errno == errno.EEXIST and os.path.isdir(directory):
            pass
        else:
            raise


if __name__ == '__main__':
    main()
