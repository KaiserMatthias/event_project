# pages/urls.py
from django.urls import path
from pages.views import home

app_name = "pages"


urlpatterns = [
    # example.com/
    path("", home, name="home"),
]
