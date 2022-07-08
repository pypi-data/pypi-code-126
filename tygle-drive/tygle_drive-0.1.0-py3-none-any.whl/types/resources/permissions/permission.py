from typing import Literal, Optional

from tygle.apis.drive.types.enums.permissions import DisplayName, Role, Type
from tygle.base import Resource
from pydantic import Field

from .permission_details import PermissionDetails


class Permission(Resource):
    kind: Literal["drive#permission"] = Field(
        "drive#permission",
        description='Identifies what kind of resource this is. Value: the fixed string "drive#permission".',
        title="kind",
    )
    id: Optional[str] = Field(
        None,
        description="The ID of this permission. This is a unique identifier for the grantee, and is published in User resources as permissionId. IDs should be treated as opaque values.",
        title="id",
    )
    type: Optional[Type] = Field(
        None,
        description="The type of the grantee. Valid values are:\nuser group domain anyone\n When creating a permission, if type is user or group, you must provide an emailAddress for the user or group. When type is domain, you must provide a domain. There isn't extra information required for a anyone type.\n\n.. note:\n    writable",
        title="type",
    )
    email_address: Optional[str] = Field(
        None,
        alias="emailAddress",
        description="The email address of the user or group to which this permission refers.\n\n.. note:\n    writable",
        title="emailAddress",
    )
    domain: Optional[str] = Field(
        None,
        description="The domain to which this permission refers.\n\n.. note:\n    writable",
        title="domain",
    )
    role: Optional[Role] = Field(
        None,
        description="The role granted by this permission. While new values may be supported in the future, the following are currently allowed:\nowner organizer fileOrganizer writer commenter reader\n\n.. note:\n    writable",
        title="role",
    )
    allow_file_discovery: Optional[bool] = Field(
        None,
        alias="allowFileDiscovery",
        description="Whether the permission allows the file to be discovered through search. This is only applicable for permissions of type domain or anyone.\n\n.. note:\n    writable",
        title="allowFileDiscovery",
    )
    display_name: Optional[DisplayName] = Field(
        None,
        alias="displayName",
        description='The "pretty" name of the value of the permission.\nThe following is a list of examples for each type of permission:\n user - User\'s full name, as defined for their Google account, such as "Joe Smith." group - Name of the Google Group, such as "The Company Administrators." domain - String domain name, such as "thecompany.com." anyone - No displayName is present.',
        title="displayName",
    )
    photo_link: Optional[str] = Field(
        None,
        alias="photoLink",
        description="A link to the user's profile photo, if available.",
        title="photoLink",
    )
    expiration_time: Optional[str] = Field(
        None,
        alias="expirationTime",
        description="The time at which this permission will expire (RFC 3339 date-time).\nExpiration times have the following restrictions:\nThey can only be set on user and group permissions The time must be in the future The time cannot be more than a year in the future\n\n.. note:\n    writable",
        title="expirationTime",
    )
    deleted: Optional[bool] = Field(
        None,
        description="Whether the account associated with this permission has been deleted. This field only pertains to user and group permissions.",
        title="deleted",
    )
    permission_details: Optional[PermissionDetails] = Field(
        None,
        alias="permissionDetails",
        description="Details of whether the permissions on this shared drive item are inherited or directly on this item. This is an output-only field which is present only for shared drive items.",
        title="permissionDetails",
    )
    view: Optional[str] = Field(
        None,
        description="Indicates the view for this permission. Only populated for permissions that belong to a view. published is the only supported value.\n\n.. note:\n    writable",
        title="view",
    )
    pending_owner: Optional[bool] = Field(
        None,
        alias="pendingOwner",
        description="Whether the account associated with this permission is a pending owner. Only populated for user type permissions for files that are not in a shared drive.\n\n.. note:\n    writable",
        title="pendingOwner",
    )
