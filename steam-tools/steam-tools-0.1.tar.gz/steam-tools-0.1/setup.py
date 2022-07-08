#!/usr/bin/env python
#
# Lara Maia <dev@lara.monster> 2015 ~ 2022
#
# The Steam Tools NG is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# The Steam Tools NG is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see http://www.gnu.org/licenses/.
#

from setuptools import setup

setup(
    name='steam-tools',
    version='0.1',
    description="Some useful tools to use with steam client or compatible programs and websites.",
    author='Lara Maia',
    author_email='dev@lara.monster',
    url='http://github.com/ShyPixie/steam-tools-ng',
    license='GPLv3',
    keywords='steam valve',
    install_requires=["steam-tools-ng"],
)