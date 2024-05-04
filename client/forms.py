# forms.py

from django import forms
from .models import route, client
from .models import CustomUser


class CreateIRouteForm(forms.ModelForm):
    class Meta:
        model = route
        fields = ['name','code','visitor']

    def __init__(self, *args, **kwargs):
        super(CreateIRouteForm, self).__init__(*args, **kwargs)
        self.fields['visitor'].queryset = CustomUser.objects.filter(is_active=True, groups__name='visitor')
        print(self.fields)


class ClientForm(forms.ModelForm):
    class Meta:
        model = client
        exclude  = ('status','create_date')