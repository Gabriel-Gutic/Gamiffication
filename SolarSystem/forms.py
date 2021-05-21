from django import forms
from django.forms import CharField


class ProposeForm(forms.Form):
    variant_1 = forms.CharField(label="Variant 1", max_length=500)
    variant_2 = forms.CharField(label="Variant 2", max_length=500)
