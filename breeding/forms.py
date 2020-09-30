from django import forms
from .models import Falcon, Pair


class FalconCreateForm(forms.ModelForm):
    """Form definition for FalconCreate."""

    class Meta:
        """Meta definition for FalconCreateform."""

        model = Falcon
        exclude = ("owner",)


class FalconUpdateForm(forms.ModelForm):
    """Form definition for FalconUpdate."""

    class Meta:
        """Meta definition for FalconUpdateform."""

        model = Falcon
        exclude = ("owner",)


class PairCreateForm(forms.ModelForm):
    """Form definition for PairCreate."""

    class Meta:
        """Meta definition for PairCreateform."""

        model = Pair
        exclude = ("owner",)


class PairUpdateForm(forms.ModelForm):
    """Form definition for PairUpdate."""

    class Meta:
        """Meta definition for PairUpdateform."""

        model = Pair
        exclude = ("owner",)