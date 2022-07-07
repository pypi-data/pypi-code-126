"""Describe dictionaries filter types."""

from __future__ import annotations

from devind_dictionaries.models import BudgetClassification, District, Organization, Region
from strawberry import auto
from strawberry_django_plus import gql


@gql.django.filter(BudgetClassification)
class BudgetClassificationFilter:
    """Filter of Budget classification."""

    id: gql.ID    # noqa
    code: auto


@gql.django.filter(District)
class DistrictFilter:
    """Filter of District."""

    name: auto


@gql.django.filter(Region)
class RegionFilter:
    """Type of Region."""

    name: auto
    common_id: auto


@gql.django.filter(Organization)
class OrganizationFilter:
    """Filter of Organization."""

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
    parent: OrganizationFilter | None
    region: RegionFilter | None
