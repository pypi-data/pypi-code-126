
# This file was generated by 'versioneer.py' (0.23.dev0) from
# revision-control system data, or from the parent directory name of an
# unpacked source archive. Distribution tarballs contain a pre-generated copy
# of this file.

import json

version_json = '''
{
 "date": "2022-07-03T20:00:07-0500",
 "dirty": false,
 "error": null,
 "full-revisionid": "77bb152333fc641df446c98c3fdd87d2e47dbfc5",
 "version": "2.7.4.dev20220706"
}
'''  # END VERSION_JSON


def get_versions():
    return json.loads(version_json)
