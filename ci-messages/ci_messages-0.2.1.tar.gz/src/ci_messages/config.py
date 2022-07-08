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

"""Configuration file handling for ci_messages."""

from configparser import ConfigParser
import os

# Read in config from /etc/python-ci_messages.conf or
# ~/.config/python-ci_messages.conf after setting a default value.
CONFIG = ConfigParser()
CONFIG.add_section("main")
CONFIG.set("main", "schemapath", "/usr/share/message-schemas/ci")

CONFIG.read("/etc/python-ci_messages.conf")
CONFIG.read(f"{os.path.expanduser('~')}/.config/python-ci_messages.conf")


# vim: set textwidth=120 ts=8 et sw=4:
