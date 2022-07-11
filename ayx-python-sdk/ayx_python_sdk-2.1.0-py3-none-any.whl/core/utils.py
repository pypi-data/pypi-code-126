# Copyright (C) 2022 Alteryx, Inc. All rights reserved.
#
# Licensed under the ALTERYX SDK AND API LICENSE AGREEMENT;
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.alteryx.com/alteryx-sdk-and-api-license-agreement
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Utility functions definitions for plugin SDK."""

import pyarrow as pa


def is_spatial(metadata: "pa.Metadata") -> bool:
    """Return true if the given arrow type is a spatial object (string + 'ayx' meta info)."""
    return metadata.get(b"ayx.source", None) == b"WKT"
