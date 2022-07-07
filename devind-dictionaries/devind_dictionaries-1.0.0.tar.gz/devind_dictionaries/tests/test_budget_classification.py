"""Module for testing budget classification."""

from datetime import datetime, timedelta

from devind_dictionaries.models import BudgetClassification
from django.core.management import call_command
from django.test import TestCase
from django.utils.timezone import make_aware
from strawberry_django_plus.test.client import Response, TestClient


COUNT_BUDGET_CLASSIFICATION_CODE = 378
COUNT_CHANGE_CODES = 10

ACTIVE_BUDGET_CLASSIFICATIONS = """
    query {
      activeBudgetClassifications {
        totalCount
        pageInfo {
          hasNextPage
          hasPreviousPage
          startCursor
          endCursor
          __typename
        }
        edges {
          node {
            id
            __typename
          }
        }
      }
    }
"""


class TestBudgetClassification(TestCase):
    """Testing budget classification."""

    def setUp(self) -> None:
        """Setuping test settings."""
        call_command('loaddata', 'budget_classification')
        self.client = TestClient('/graphql/')

    def test_invoke_command(self) -> None:
        """Testing invoke command python manage.py load_budget_classification."""
        self.assertEqual(BudgetClassification.objects.count(), COUNT_BUDGET_CLASSIFICATION_CODE)

    def test_budget_classifications(self) -> None:
        """Test budget classification relay query."""
        query = """
          query {
            budgetClassifications {
              totalCount
              pageInfo {
                hasNextPage
                hasPreviousPage
                startCursor
                endCursor
                __typename
              }
              edges {
                node {
                  id
                  __typename
                }
              }
            }
          }
        """
        response: Response = self.client.query(query)
        self.assertIsNone(response.errors)
        budget_classification: dict[str, str | dict] | None = response.data.get('budgetClassifications')
        self.assertIsNotNone(budget_classification)
        self.assertEqual(budget_classification['totalCount'], COUNT_BUDGET_CLASSIFICATION_CODE)

    def test_active_budget_classifications(self) -> None:
        """Testing active budget classifications."""
        response: Response = self.client.query(ACTIVE_BUDGET_CLASSIFICATIONS)
        self.assertIsNone(response.errors)
        budget_classifications: dict[str, str | dict] | None = response.data.get('activeBudgetClassifications')
        self.assertIsNotNone(budget_classifications)
        self.assertEqual(budget_classifications['totalCount'], COUNT_BUDGET_CLASSIFICATION_CODE)

    def test_active_budget_classification(self) -> None:
        """Testing active flag in budget classification."""
        budget_classifications_ids: list[int] = BudgetClassification.objects \
            .values_list('id', flat=True)[:COUNT_CHANGE_CODES]
        self.assertEqual(len(budget_classifications_ids), COUNT_CHANGE_CODES)
        BudgetClassification.objects.filter(pk__in=budget_classifications_ids).update(active=False)
        response: Response = self.client.query(ACTIVE_BUDGET_CLASSIFICATIONS)
        self.assertIsNone(response.errors)
        budget_classifications: dict[str, str | dict] | None = response.data.get('activeBudgetClassifications')
        self.assertIsNotNone(budget_classifications)
        self.assertEqual(budget_classifications['totalCount'], COUNT_BUDGET_CLASSIFICATION_CODE - COUNT_CHANGE_CODES)

    def test_end_budget_classification_back(self) -> None:
        """Testing end date in budget classification."""
        end = datetime.now() - timedelta(days=2)
        budget_classifications_ids: list[int] = BudgetClassification.objects \
            .values_list('id', flat=True)[:COUNT_CHANGE_CODES]
        self.assertEqual(len(budget_classifications_ids), COUNT_CHANGE_CODES)
        BudgetClassification.objects.filter(pk__in=budget_classifications_ids).update(end=make_aware(end))
        response: Response = self.client.query(ACTIVE_BUDGET_CLASSIFICATIONS)
        self.assertIsNone(response.errors)
        budget_classification: dict[str, str | dict] | None = response.data.get('activeBudgetClassifications')
        self.assertIsNotNone(budget_classification)
        self.assertEqual(budget_classification['totalCount'], COUNT_BUDGET_CLASSIFICATION_CODE - COUNT_CHANGE_CODES)

    def tearDown(self) -> None:
        """Delete all budget classification code."""
        BudgetClassification.objects.all().delete()
