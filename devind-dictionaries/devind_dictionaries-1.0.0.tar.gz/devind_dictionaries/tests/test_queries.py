"""Test queries."""

from django.test import TestCase
from strawberry_django_plus.test.client import Response, TestClient

from .test_services import get_test_organizations
from ..models import District, Organization, Region
from ..services import parse_organizations, update_entity


class TestQueries(TestCase):
    """Testing queries."""

    def setUp(self) -> None:
        """Set up data for testing."""
        content = get_test_organizations()
        districts, regions, organizations = parse_organizations(content)
        update_entity(District, districts)
        update_entity(Region, regions)
        update_entity(Organization, organizations)

        self.client = TestClient('/graphql/')

    def test_district(self) -> None:
        """Testing district query."""
        query: str = """
          query ($pk: ID!) {
            district (pk: $pk) {
              id
              name
              __typename
            }
          }
        """
        response: Response = self.client.query(query, {'pk': 1})
        self.assertIsNone(response.errors)
        district: dict[str, str] | None = response.data.get('district')
        self.assertIsNotNone(district)
        self.assertEqual(district['__typename'], 'DistrictType')

    def test_districts(self) -> None:
        """Testing districts query."""
        response: Response = self.client.query(
            """
            query {
              districts {
                id
                name
                __typename
              }
            }
            """
        )
        self.assertIsNone(response.errors)
        districts: list[dict[str, str]] | None = response.data.get('districts')
        self.assertIsNotNone(districts)
        self.assertEqual(len(districts), District.objects.count())

    def tearDown(self) -> None:
        """Free seeder data."""
        Organization.objects.all().delete()
        Region.objects.all().delete()
        District.objects.all().delete()
