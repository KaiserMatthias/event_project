from django.shortcuts import render
from events.models import Event, Category


def home(request):
    """Dashboard des Projekts.

    127.0.0.1:8000
    """
    context = {
        "events": Event.objects.all()[:2],
        "categories": Category.objects.all(),
    }

    return render(
        request,
        "pages/index.html",
        context,
    )
