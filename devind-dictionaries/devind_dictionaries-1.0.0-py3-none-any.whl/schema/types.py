"""Describe dictionaries types."""

from __future__ import annotations

import datetime

import strawberry
from devind_dictionaries.models import BudgetClassification, Department, District, Organization, Region
from strawberry import auto
from strawberry_django_plus import gql

from .filters import BudgetClassificationFilter, DistrictFilter, OrganizationFilter, RegionFilter


class BaseTimeStamps:
    """Base of timeStamps class."""

    created_at: datetime.datetime
    updated_at: datetime.datetime


@gql.django.type(BudgetClassification, filters=BudgetClassificationFilter)
class BudgetClassificationType(BaseTimeStamps, gql.relay.Node):
    """Type of Budget classification."""

    id: gql.ID  # noqa
    code: auto
    name: auto
    active: auto
    start: auto
    end: auto


@gql.django.type(Department)
class DepartmentType(BaseTimeStamps):
    """Type of Departments."""

    id: gql.ID  # noqa
    name: auto
    code: auto

    # user: UserType | None # noqa
    # minister: UserType | None  # noqa
    #
    # @gql.django.field  # (only=['users'])
    # def users(self, root: Department) -> 'list[UserType]':
    #     """Resolve function for users in Departments."""
    #     return root.users.all()    # noqa

    @gql.django.field
    def organizations(self, root: Department) -> 'list[OrganizationType]':
        """Resolve function for organizations in Departments."""
        return root.organizations.all()


@gql.django.type(District, filters=DistrictFilter)
class DistrictType(BaseTimeStamps):
    """Type of District."""

    id: gql.ID  # noqa
    name: auto

    @gql.django.field   # (only='region_set')
    def regions(self, root: District) -> 'list[RegionType]':
        """Resolve function for Regions in District."""
        return root.region_set.all()


@gql.django.type(Region, filters=RegionFilter)
class RegionType(BaseTimeStamps):
    """Type of Region."""

    id: gql.ID  # noqa
    name: auto
    common_id: auto
    district: DistrictType | None


@gql.django.type(Organization, filters=OrganizationFilter)
class OrganizationType(BaseTimeStamps, gql.relay.Node):
    """Type of Organization."""

    id: gql.ID  # noqa
    name: auto
    present_name: auto
    inn: auto
    kpp: auto
    kind: auto
    rubpnubp: auto
    kodbuhg: auto
    okpo: auto
    phone: auto
    site: auto
    mail: auto
    address: auto
    attributes: strawberry.scalars.JSON
    parent: 'OrganizationType | None'
    region: RegionType | None
    # user: UserType  # noqa
    #
    # @gql.django.field  # (only=['users']) # noqa
    # def users(self, root: Organization) -> 'list[UserType]': # noqa
    #     """Resolve function for users in Departments.""" # noqa
    #     return root.users.all() # noqa
