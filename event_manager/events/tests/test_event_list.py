"""
Testen der Übersicht der Events

uv run pytest -s  => prints ausgeben
uv run pytest -v => Verbose (bessere Ausgabe)
"""

from datetime import timedelta

from django.db.models import QuerySet
from django.utils import timezone
from django.urls import reverse
from django.test import Client
import pytest

from events.models import Event, Category


@pytest.mark.django_db
def test_event_list_view(client: Client, event_obj_list: QuerySet[Event]):
    """Testen der Übersicht der Events.
    event_list ist ein Fixture aus conftest (wird nur dazu benötigt,
    um Objekte in der DB anzulegen)

    Testen:
    - Statuscode
    - Template-Name
    """

    # URL anlegen und via client einen GET-Request abfeuern
    url = reverse("events:event-list")
    response = client.get(url)

    # Behauptungen
    assert response.status_code == 200
    # assert "events/event_list.html" in [t.name for t in response.templates]
    assert "events/event_list.html" in response.template_name
    # Wurden auch 2 Objekte in der Liste ausgeben
    assert response.context["object_list"].count() == 2
    assert "Übersicht der Events" in response.content.decode()

    # print(vars(response))  # gib alles, was das Response Objekt hat, aus

    # {% url "events:category-detail" category.id %}
    # url = reverse("events:category-detail", args=[category.id])
