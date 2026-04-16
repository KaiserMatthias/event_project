# events/tests/test_category.py

# @pytest.mark.django_db => nutzt
from django.urls import reverse
from django.test import Client
import pytest

from events.models import Category


@pytest.mark.django_db
def test_create_category_valid_input(client: Client):
    """Testen, ob eine Kategorie mit validem Input erfolgreich angelegt wird."""

    # Formular-Inhalt:
    payload = {
        "name": "Test Category",
        "sub_title": "ein Subtitle",
        "description": "Kategorie Beschreibung",
    }

    url = reverse("events:category-create")
    # Sende Daten an category-create Endpunkt
    response = client.post(url, payload)  # html post

    # StatusCode 302: nach Eintragen in DB wird weitergeleitet an Detailseite
    assert response.status_code == 302

    # Testen, ob das Objekt eingetragen wurde.
    # Da jeder Test isoliert ist, darf nur 1 Objekt in der DB sein
    assert Category.objects.count() == 1

    # Objekct aus DB holen
    category = Category.objects.first()
    assert category.name == "Test Category"


@pytest.mark.django_db
def test_category_detail_view(client: Client, category_obj: Category):
    """Testen ob eine Kategorie via Web erreichbar ist."""
    # Kategorie Objekt in der DB anlegen
    # statt ein Objekt selbst zu definieren, bekommen wir es via fixture
    # siehe conftest.py
    # test_category = Category.objects.create(name="Test XXX Category")

    # http://127.0.0.1:8000/events/categories/1
    # "events:category-detail" => events/categories/1
    url = reverse("events:category-detail", args=[category_obj.pk])

    # Client (Browser) feuert get Request ab
    response = client.get(url)

    # Behauptungen (StatusCode, Template-Name, Kategorie-Name)
    assert response.status_code == 200
    assert "events/category_detail.html" in [t.name for t in response.templates]
    # ist der Name Test XXX Category auch wirklich im Response-Objekt enthalten (aka Website)
    assert "Test XXX Category" in response.content.decode(encoding="utf-8")

    # => ein langer Text (Website Quellcode, html, js, css)
    # print(response.content.decode(encoding="utf-8"))
