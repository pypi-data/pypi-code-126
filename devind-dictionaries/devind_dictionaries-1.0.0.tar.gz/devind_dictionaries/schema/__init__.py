"""Description for dictionaries schema."""
from typing import Iterable

from strawberry_django_plus import gql
from strawberry_django_plus.permissions import HasPerm

from .filters import BudgetClassificationFilter
from .types import BudgetClassificationType, DepartmentType, DistrictType, OrganizationType, RegionType
from ..services import get_active_budget_classification
from ..tasks import update_organizations


@gql.type
class Query:
    """List of queries for dictionaries."""

    budget_classifications: gql.relay.Connection[BudgetClassificationType] = gql.django.connection(
        description='Доступные коды бюджетной классификации'
    )

    @gql.django.connection(
        description='Активные коды бюджетной классификации'
    )
    def active_budget_classifications(self) -> Iterable[BudgetClassificationType]:
        """Get active budget classifications."""
        return get_active_budget_classification()

    department: DepartmentType = gql.django.field()
    departments: list[DepartmentType] = gql.django.field()

    district: DistrictType = gql.django.field()
    districts: list[DistrictType] = gql.django.field()

    region: RegionType = gql.django.field()
    regions: list[RegionType] = gql.django.field()

    organization: OrganizationType = gql.django.field()
    organizations: gql.relay.Connection[OrganizationType] = gql.django.connection(
        description='Доступные организации'
    )


@gql.type
class Mutation:
    """List of mutations for dictionaries."""

    @gql.mutation(directives=[
        HasPerm('devind_dictionaries.change_district'),
        HasPerm('devind_dictionaries.change_region'),
        HasPerm('devind_dictionaries.change_organization'),
    ])
    def update_organization(self) -> bool:
        """Start celery task."""
        update_organizations.delay()
        return True
