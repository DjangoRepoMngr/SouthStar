# forms.py

from django import forms
from .models import route
from django.contrib.auth.models import User


class CreateIRouteForm(forms.ModelForm):
    class Meta:
        model = route
        fields = ['name','code','visitor']

    def __init__(self, *args, **kwargs):
        super(CreateIRouteForm, self).__init__(*args, **kwargs)
        self.fields['visitor'].queryset = User.objects.filter(is_active=True, groups__name='visitor')
        print(self.fields)

        # Override label_from_instance method to display full names
        self.fields['visitor'].label_from_instance = self.label_user_from_instance

    def label_user_from_instance(self, obj):
        return obj.get_full_name() if obj.get_full_name() else obj.username
