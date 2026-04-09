# events/admin.py => stellt Formulare für die Adminoberfläche zur Verfügung
from django.contrib import admin
from events.models import Category, Event

# Model für Admin registrieren
admin.site.register(Category)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """
    Der @admin.register Dekorator bindet das Event-Model
    an die Klasse EventAdmin, die von der Klasse ModelAdmin erbt.

    Damit lässt sich die AdminOberfläche deutlich verbessern
    https://djangoheroes.friendlybytes.net/organisation/admin_extend.html
    """

    # mehr Infos in der Übersicht
    list_display = ["id", "name", "category"]
