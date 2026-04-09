# events/urls.py (URLs der Event-App)
from django.urls import path
from .views import categories, category_detail

# ist nötig für den url-tag im Template: app_name:path_name,
# z.B. events:category-detail
app_name = "events"

# hier liegen die anderen Pfad-Teile
urlpatterns = [
    # /events/categories
    path("categories", categories, name="categories"),
    # /events/categories/3
    # <int:pk> => matche Integer, das Keyword-Argument lautet pk
    path("categories/<int:pk>", category_detail, name="category-detail"),
]


# Kategorie-Detail, wenn der Pfad match, wir die View
# so aufgerufen
# category_detail(pk=34)
# Aufgabe
# Es sollen alle Lieferadressesen / Notizen in einer Liste dargestellt werden
# Entwerfe dazu
# View, Urls.py, Template
#
