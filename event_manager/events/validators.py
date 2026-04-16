"""
selbstdefinierte Validatoren
"""

from datetime import timedelta, datetime

from django.core.exceptions import ValidationError
from django.utils import timezone


def datetime_in_future(date_input: datetime) -> None:
    """
    Wenn dateintput in der Vergangenheit
    liegt, soll ein ValidationError ausgelöst werden.
    """
    if date_input < timezone.now() + timedelta(hours=1):
        raise ValidationError("The date must be at least one hour in the future.")
