from django import forms
from .models import Falcon, Office, Pair, Aviary, Birth_cert


class FalconCreateForm(forms.ModelForm):
    """Form definition for FalconCreate."""

    class Meta:
        """Meta definition for FalconCreateform."""

        model = Falcon
        exclude = ("owner",)
        widgets = {"birth_date": forms.DateTimeInput(attrs={"type": "date"})}


class YoungFalconCreateForm(forms.ModelForm):
    """Form definition for FalconCreate."""

    class Meta:
        """Meta definition for FalconCreateform."""

        model = Falcon
        exclude = ("owner", "father", "mother")
        widgets = {"birth_date": forms.DateTimeInput(attrs={"type": "date"})}


class FalconUpdateForm(forms.ModelForm):
    """Form definition for FalconUpdate."""

    class Meta:
        """Meta definition for FalconUpdateform."""

        model = Falcon
        exclude = ("owner",)
        widgets = {"birth_date": forms.DateTimeInput(attrs={"type": "date"})}


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
        widgets = {"last_cleaned": forms.DateTimeInput(attrs={"type": "date"})}


class AviaryUpdateForm(forms.ModelForm):
    """Form definition for AviaryUpdate."""

    class Meta:
        """Meta definition for AviaryUpdateForm."""

        model = Aviary
        exclude = ("owner",)
        widgets = {"last_cleaned": forms.DateTimeInput(attrs={"type": "date"})}


class Birth_certCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)
        self.fields['falcons'] = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            choices=(((choice.id), choice) for choice in Falcon.objects.all())
        )

    class Meta:

        model = Birth_cert
        exclude = ("owner", "cert_file")
        widgets = {"issued_date": forms.DateTimeInput(attrs={"type": "date"})}


class Birth_certUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['falcons'] = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            choices=(((choice.id), choice) for choice in Falcon.objects.all())
        )

    class Meta:

        model = Birth_cert
        exclude = ("owner",)
        widgets = {"issued_date": forms.DateTimeInput(attrs={"type": "date"})}


class OfficeCreateForm(forms.ModelForm):

    class Meta:

        model = Office
        exclude = ("owner",)


class OfficeUpdateForm(forms.ModelForm):

    class Meta:

        model = Office
        exclude = ("owner",)
