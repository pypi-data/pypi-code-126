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

# these are all kinda inappropriate for pytest patterns
# pylint: disable=no-init, protected-access, no-self-use, unused-argument, too-many-public-methods

"""Tests for the schema implementation."""

# stdlib imports
import json
import os

# internal imports
import ci_messages.schema


def _load_example(topic):
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "examples", topic) + ".json"
    with open(path) as fhand:
        body = json.load(fhand)
    return ci_messages.schema.CIMessageV1(topic=topic, body=body)


class TestSchemas(object):
    def test_productmd_compose(self):
        """Tests for a productmd-compose.test.complete message."""
        testmsg = _load_example("productmd-compose.test.complete")
        testmsg.validate()
        assert (
            str(testmsg)
            == "CI: acceptance test of productmd-compose RHEL-ALT-7-20180101.n.0 finished"
        )
        assert (
            testmsg.url
            == "https://rtt.somewhere.com/job/compose-RHEL-ALT-7-nightly-tier2-acceptance/arch=aarch64,variant=Server/1/"
        )

    def test_brew_build(self):
        """Tests for a brew-build.promote.queued message."""
        testmsg = _load_example("brew-build.promote.queued")
        testmsg.validate()
        assert str(testmsg) == "CI: promotion of brew-build setup-2.8.71-7.el7_4 was queued"
        # Hmm. Do we get clever with artifact['source']?
        assert testmsg.url == ""

    def test_uncontrolled_build_build(self):
        """Tests for a uncontrolled-build.build.complete message."""
        testmsg = _load_example("uncontrolled-build.build.complete")
        testmsg.validate()
        assert (
            str(testmsg)
            == "CI: build of uncontrolled-build plymouth-theme-hot-dog-0.4-1.fc16 finished"
        )
        assert (
            testmsg.url
            == "https://wwoods.fedorapeople.org/hot-dog/plymouth-theme-hot-dog-0.4-1.fc16.noarch.rpm"
        )

    def test_uncontrolled_build_test(self):
        """Tests for a uncontrolled-build.test.complete message."""
        testmsg = _load_example("uncontrolled-build.test.complete")
        testmsg.validate()
        assert (
            str(testmsg)
            == "CI: tier1 test of uncontrolled-build plymouth-theme-hot-dog-0.4-1.fc16 finished"
        )
        assert testmsg.url == "http://wizard.zone/job/hot-dog/1337"

    def test_fedora_update(self):
        """Tests for a fedora-update.test.complete message."""
        testmsg = _load_example("fedora-update.test.complete")
        testmsg.validate()
        assert (
            str(testmsg)
            == "CI: install_default_update_live uefi updates-workstation-live-iso x86_64 test of fedora-update FEDORA-2019-6bda4c81f4 finished"
        )
        assert testmsg.url == "https://openqa.stg.fedoraproject.org/tests/583271"


# vim: set textwidth=120 ts=8 et sw=4:
