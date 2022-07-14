# ----------------------------------------------------------------------------
# Copyright (C) 2021-2022 runml_checks (https://www.runml_checks.com)
#
# This file is part of runml_checks.
# runml_checks is distributed under the terms of the GNU Affero General
# Public License (version 3 or later).
# You should have received a copy of the GNU Affero General Public License
# along with runml_checks.  If not, see <http://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------------
#
"""
Module for anonymous telemetry.

No credentials, data, personal information or anything private is collected (and will never be).
"""
import http.client
import os
import pathlib
import uuid

import runml_checks

MODULE_DIR = pathlib.Path(__file__).absolute().parent.parent
ANALYTICS_DISABLED = os.environ.get('DISABLE_runml_checks_ANONYMOUS_TELEMETRY', False)


def send_anonymous_import_event():
    """Send an anonymous import event to PostHog."""
    if not ANALYTICS_DISABLED:
        try:
            if os.path.exists(os.path.join(MODULE_DIR, '.user_id')):
                with open(os.path.join(MODULE_DIR, '.user_id'), 'r', encoding='utf8') as f:
                    user_id = f.read()
            else:
                user_id = str(uuid.uuid4())
                with open(os.path.join(MODULE_DIR, '.user_id'), 'w', encoding='utf8') as f:
                    f.write(user_id)

            conn = http.client.HTTPSConnection('api.runml_checks.com', timeout=3)
            conn.request('GET', f'/metrics?version={runml_checks.__version__}&uuid={user_id}')
            _ = conn.getresponse()
        except Exception:  # pylint: disable=broad-except
            pass
