# forms.py

from django import forms
from .models import route


class CreateIRouteForm(forms.ModelForm):
    class Meta:
        model = route
        fields = ['name','code']
