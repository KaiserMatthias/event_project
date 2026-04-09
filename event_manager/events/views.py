# events/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Category, Event


def category_detail(request, pk: int):
    """Eine Kategorie-Detailseite.

    events/categories/3
    """
    # category = Category.objects.get(pk=pk)
    # Hole Objekt oder löse 404 Fehler aus
    category = get_object_or_404(Category, pk=pk)
    return render(
        request,
        "events/category_detail.html",
        {
            "category": category,
        },
    )


def categories(request):
    """Auflisten aller Kategorien.

    events/categories
    """
    qs = Category.objects.all()
    context = {"categories": qs}

    return render(
        request,
        "events/categories.html",
        context,
    )


def qs_test(request):
    """Eine Funktion zum Testen von Queries.
    akutell nicht per URL erreichbar (keine Verlinkung)
    """
    # Alle Kategorie-Objekte selektieren (Select * from event_category)
    qs = Category.objects.all()
    print(f"Alle Kategorien: {qs}")

    # Alle Kategorien die mit dem Buchstaben K anfangen
    # Select * from categeory where name LIKE "K%" and name LIKE "%o"
    # Filter resultieren immer in UND
    qs = Category.objects.all()  # keine DB-Anfrage
    qs = qs.filter(name__startswith="K")
    qs = qs.filter(name__endswith="o")
    print(f"Alle Kategorien mit K: {qs}")
    print(f"SQL-Abfrage: {str(qs.query)}")  # Zeigt die eigentliche SQL-Anfrage

    # Ein Objekt selektieren
    # Objekt mit ID 1 (pk mappt auf Primary Key)
    sport = Category.objects.get(pk=1)
    # alle Sport-Events (über das Kategorie-Objekt via related_name aus Model
    # kann man alle Events selektieren, die der Kategorie zugeteilt sind
    sport_events = sport.events.all()  # type: ignore
    print("Sport Objekte:", sport_events)

    anzahl_events: int = Event.objects.count()
    print("Anzahl Event in der DB:", anzahl_events)

    events_mit_s = Event.objects.all().filter(name__contains="s")
    print(events_mit_s)

    # Alle Kategorien, deren Events ein kleines s im Namen haben
    categories_mit_s = Category.objects.filter(events__name__contains="s")
    print("Kategorien mit Events mit s:", categories_mit_s)
    print("SQL:", str(categories_mit_s.query))

    return HttpResponse("-".join(map(str, qs)))
