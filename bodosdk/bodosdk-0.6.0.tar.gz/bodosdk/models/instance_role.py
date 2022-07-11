from typing import List, Dict, Optional, Any, Union
from uuid import UUID

import pydantic
from pydantic import Field

from bodosdk.models.base import CamelCaseBase
from bodosdk.models.cluster import ClusterMetadata

class InstanceRole(CamelCaseBase):
    role_arn: str # only available for AWS

class InstanceRoleItem(CamelCaseBase):
    name: str
    uuid: str
    status: str
    description: str

class CreateRoleDefinition(CamelCaseBase):
    name: str
    description: str
    data: InstanceRole

class CreateRoleResponse(CreateRoleDefinition):
    uuid: str
    status: str