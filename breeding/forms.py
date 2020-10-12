from django import forms
from .models import Falcon, Pair, Aviary


class FalconCreateForm(forms.ModelForm):
    """Form definition for FalconCreate."""

    class Meta:
        """Meta definition for FalconCreateform."""

        model = Falcon
        exclude = ("owner",)


class YoungFalconCreateForm(forms.ModelForm):
    """Form definition for FalconCreate."""

    class Meta:
        """Meta definition for FalconCreateform."""

        model = Falcon
        exclude = ("owner", "father", "mother")


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
        exclude = ()


class PairUpdateForm(forms.ModelForm):
    """Form definition for PairUpdate."""

    class Meta:
        """Meta definition for PairUpdateform."""

        model = Pair
        exclude = ()


class AviaryCreateForm(forms.ModelForm):
    """Form definition for AviaryCreate."""

    class Meta:
        """Meta definition for AviaryCreateForm."""

        model = Aviary
        exclude = ("owner",)


class AviaryUpdateForm(forms.ModelForm):
    """Form definition for AviaryUpdate."""

    class Meta:
        """Meta definition for AviaryUpdateForm."""

        model = Aviary
        exclude = ("owner",)
