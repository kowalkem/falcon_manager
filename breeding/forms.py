from django import forms
from .models import Falcon


class FalconCreateForm(forms.ModelForm):
    """Form definition for FalconCreate."""

    class Meta:
        """Meta definition for FalconCreateform."""

        model = Falcon
        exclude = ('owner',)


class FalconUpdateForm(forms.ModelForm):
    """Form definition for FalconUpdate."""

    class Meta:
        """Meta definition for FalconUpdateform."""

        model = Falcon
        exclude = ('owner',)
