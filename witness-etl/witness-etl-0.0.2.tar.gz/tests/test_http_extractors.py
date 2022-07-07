

#  Copyright (c) 2022.  Eugene Popov.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

import pytest
from tests import mock_dir, xfail, parametrize
from witness.extractors.http import JsonHttpGetExtractor


mock_uri = 'http://example.com'
mock_params = {}


extractor = JsonHttpGetExtractor(uri=mock_uri, params=mock_params)


def test_extract():
    extractor.extract()
    print(extractor.output)


def test_unify():
    extractor.extract().unify()
    print(extractor.output)
