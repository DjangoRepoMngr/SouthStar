# forms.py

from django import forms
from .models import route, client
from .models import CustomUser, SupervisorVisitorRelationship


class CreateIRouteForm(forms.ModelForm):
    class Meta:
        model = route
        fields = ['name','code','visitor']


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the user from the kwargs
        super(CreateIRouteForm, self).__init__(*args, **kwargs)


        if user.groups.filter(name='supervisor').exists():
                # Filter visitors who are supervised by this supervisor
                supervisees = SupervisorVisitorRelationship.objects.filter(supervisor=user).values_list('visitor', flat=True)
                self.fields['visitor'].queryset = CustomUser.objects.filter(
                    id__in = supervisees
                )
        elif user.groups.filter(name='visitor').exists():
                # Set the visitor field to only the current user
                self.fields['visitor'].queryset = CustomUser.objects.filter(id=user.id)



class ClientForm(forms.ModelForm):
    class Meta:
        model = client
        exclude  = ('status','create_date')