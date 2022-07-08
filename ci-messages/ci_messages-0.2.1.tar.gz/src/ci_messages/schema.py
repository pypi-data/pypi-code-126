# Copyright Red Hat
#
# This file is part of python-ci_messages.
#
# python-ci_messages is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Adam Williamson <awilliam@redhat.com>

"""fedora-messaging schema wrapper for CI Messages schemas."""

# standard libraries
import os

# External dependencies
from fedora_messaging import message
import jsonref

# Internal dependencies
from .config import CONFIG


class CIMessageV1(message.Message):
    """
    Message class for messages conforming to the CI Messages spec:
    https://pagure.io/fedora-ci/messages
    """

    @property
    def _stripped_split_topic(self):
        """Gives us the topic portion without any prefix parts, split
        on periods, so for 'org.centos.prod.ci.koji-build.test.queued'
        it gives us ('koji-build', 'test', 'queued') - this maps to
        (artifact, event, status).
        """
        return self.topic.split(".")[-3:]

    def __str__(self):
        """We just use the summary for now."""
        return self.summary

    @property
    def body_schema(self):
        """Read the schema from the appropriate file, based on the
        message topic.
        """
        # ditch any prefixes from the topic, e.g.
        # org.centos.prod.ci.koji-build.test.queued
        topic = ".".join(self._stripped_split_topic)
        schema_path = CONFIG.get("main", "schemapath")
        fname = os.path.join(schema_path, topic) + ".json"
        with open(fname, "r") as fhand:
            return jsonref.load(fhand, base_uri=f"file://{schema_path}/", jsonschema=True)

    @property
    def artifact_id(self):
        """Most useful identifier for the artifact."""
        artifact = self.body.get("artifact", {})
        aid = artifact.get("descriptor")
        if not aid:
            aid = artifact.get("nvr")
        if not aid:
            # for fedora-update
            aid = artifact.get("alias")
        if not aid:
            aid = artifact.get("id")
        if not aid:
            aid = "<unknown>"
        return aid

    @property
    def summary(self):
        """A summary of the message."""
        (artifact, event, status) = self._stripped_split_topic
        # grammar!
        if event == "promote":
            event = "promotion"
        if event == "test":
            ttype = self.body.get("test", {}).get("type")
            if ttype:
                event = ttype + " test"
        status = {
            "queued": "was queued",
            "running": "started",
            "complete": "finished",
            "error": "failed",
        }.get(status)
        aid = self.artifact_id
        return f"CI: {event} of {artifact} {aid} {status}"

    @property
    def url(self):
        """The most likely-relevant URL we can find."""
        url = self.body.get("run", {}).get("url")
        if not url:
            url = self.body.get("artifact", {}).get("url")
        if not url:
            url = ""
        return url


# vim: set textwidth=120 ts=8 et sw=4:
