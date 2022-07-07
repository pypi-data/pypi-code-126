"""Сервисы для классификации кодов бюджетной классификации."""

import datetime
from typing import Iterable

from devind_dictionaries.models import BudgetClassification
from django.db.models import Q, QuerySet
from django.utils import timezone


def get_active_budget_classification() -> Iterable[QuerySet[BudgetClassification] | BudgetClassification]:
    """Возвращает активные КБК на текущий момент."""
    now: datetime.datetime = timezone.now()
    return BudgetClassification.objects.filter(
        Q(active=True, start__lt=now) & Q(Q(end__gt=now) | Q(end__isnull=True))
    )
