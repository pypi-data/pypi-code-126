
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
from . import files_dir
import datetime
from witness.core.batch import Batch
from witness.loaders.pandas import PandasFeatherLoader, PandasExcelLoader

xfail = pytest.mark.xfail
parametrize = pytest.mark.parametrize

collect_ignore = ["setup.py", "test_database_extractors.py"]

# region mock

batch_meta = {
    'extraction_timestamp': datetime.datetime(2022, 1, 1, 12, 0, 0, 0),
    'record_source': r'calibration_data',
    'tags': ['debug', 'snapshot']
}

batch_data = [
    {'string': 'string_value_1', 'integer': 31, 'timestamp': datetime.datetime(2022, 6, 15, 11, 0, 0, 0)},
    {'string': 'string_value_2', 'integer': 14561, 'timestamp': datetime.datetime(2001, 4, 13, 12, 0, 0, 0)},
    {'string': 'string_value_3', 'integer': 7634, 'timestamp': datetime.datetime(2031, 2, 5, 15, 43, 0, 0)}
]

batches = [
    Batch(batch_data, batch_meta)
]


loaders = [
    PandasFeatherLoader(f'{files_dir}/feather_dump'),
    PandasExcelLoader(f'{files_dir}/excel_dump.xlsx')
]

# endregion mock


@pytest.fixture(params=batches)
def fxtr_batch(request):
    yield request.param


@pytest.fixture(params=loaders)
def fxtr_loader(request):
    yield request.param


