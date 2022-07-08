from typing import Optional

from tygle.apis.drive.types.enums.permissions.permission_details import (
    PermissionType,
    Role,
)
from pydantic import BaseModel, Field


class PermissionDetails(BaseModel):
    permission_type: Optional[PermissionType] = Field(
        None,
        alias="permissionType",
        description="The permission type for this user. While new values may be added in future, the following are currently possible:\nfile member",
        title="permissionType",
    )
    role: Optional[Role] = Field(
        None,
        description="The primary role for this user. While new values may be added in the future, the following are currently possible:\norganizer fileOrganizer writer commenter reader",
        title="role",
    )
    inherited_from: Optional[str] = Field(
        None,
        alias="inheritedFrom",
        description="The ID of the item from which this permission is inherited. This is an output-only field.",
        title="inheritedFrom",
    )
    inherited: Optional[bool] = Field(
        None,
        description="Whether this permission is inherited. This field is always populated. This is an output-only field.",
        title="inherited",
    )
