from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReleaseRequestModel")


@attr.s(auto_attribs=True)
class ReleaseRequestModel:
    """
    Attributes:
        name (Union[Unset, str]): Name of the release. This can be a user friendly name to identify the release.
        version (Union[Unset, str]): The version of the release. Only following three formats are allowed x.x, x.x.x,
            x.x.x.x.
        channel (Union[Unset, str]): Channel of the release. The default value is 'stable'.
        platform (Union[Unset, str]): Platform of the release. It will usually have one of the following values:
            windows, linux, macos, win32, win64 etc.
        private (Union[Unset, None, bool]): Private releases don't appear in the customer portal.
        notes (Union[Unset, None, str]): Release notes for the release. It also supports markdown.
        product_id (Union[Unset, str]): Unique identifier for the product.
    """

    name: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    channel: Union[Unset, str] = UNSET
    platform: Union[Unset, str] = UNSET
    private: Union[Unset, None, bool] = UNSET
    notes: Union[Unset, None, str] = UNSET
    product_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        version = self.version
        channel = self.channel
        platform = self.platform
        private = self.private
        notes = self.notes
        product_id = self.product_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if channel is not UNSET:
            field_dict["channel"] = channel
        if platform is not UNSET:
            field_dict["platform"] = platform
        if private is not UNSET:
            field_dict["private"] = private
        if notes is not UNSET:
            field_dict["notes"] = notes
        if product_id is not UNSET:
            field_dict["productId"] = product_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        version = d.pop("version", UNSET)

        channel = d.pop("channel", UNSET)

        platform = d.pop("platform", UNSET)

        private = d.pop("private", UNSET)

        notes = d.pop("notes", UNSET)

        product_id = d.pop("productId", UNSET)

        release_request_model = cls(
            name=name,
            version=version,
            channel=channel,
            platform=platform,
            private=private,
            notes=notes,
            product_id=product_id,
        )

        return release_request_model
