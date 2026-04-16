"""
events/tests/conftest.py

Globale Ort von Fixtures ohne Import!

Fixtures kann man nutzen, ohne zu importieren
und ohne an die Funktion als Argument zu übergeben.

"""

from datetime import timedelta

from django.db.models import QuerySet
from django.utils import timezone
import pytest

from events.models import Event, Category


@pytest.fixture
def category_obj():
    # überall, wo ich ein Kategorie-Objekt benötige, kann ich im
    # Parameterkopf einer Testfunktion den parameter category_obj eintragen
    # siehe test_category_detail_view
    return Category.objects.create(name="Test XXX Category")


@pytest.fixture
def event_obj_list(category_obj: Category) -> QuerySet[Event]:
    """Erzeuge ein Queryset von 2 Event-Objekten."""
    event_1 = Event.objects.create(
        name="Test Event 1",
        date=timezone.now() + timedelta(hours=3),
        category=category_obj,
    )
    event_2 = Event.objects.create(
        name="Test Event 2",
        date=timezone.now() + timedelta(hours=3),
        category=category_obj,
    )
    return Event.objects.all()
