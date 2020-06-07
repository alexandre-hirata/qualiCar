from django import forms

import datetime

from qualiCar_API.models import Vehicle, Part, Incident, UserProfile


class IncidentForm (forms.Form):
    part = Part.objects.all ()
    # part = forms.ChoiceField (
    #     choices = Part.objects.all (),
    #     label='Parts',
    #     # widget=forms.Select (
    #     #     attrs = {'class' : 'form-control'}
    #     # )
    # )
    description = forms.CharField (
        max_length=150,
        widget=forms.TextInput(attrs={
            'class' : 'form-control py-4',
            'placeholder' : 'Enter incident description',
        })
    )

    create_on = forms.CharField (
        widget=forms.TextInput(attrs={
            'class' : 'small mb-1 form-control',
            'value' : datetime.date.today,
            'disabled' : 'True',
        })
    )

    last_change_on = forms.CharField (
        widget=forms.TextInput(attrs={
            'class' : 'small mb-1 form-control',
            'value' : datetime.date.today,
            'disabled' : 'True',
        })
    )

    part = forms.ModelChoiceField (
        queryset = part,
        required = False,
        widget=forms.Select(attrs={
            'class' : 'mdb-select md-form',

        })
    )

    def __init__(self, *args, **kwargs):
        self.UserProfile = UserProfile

        super (IncidentForm, self).__init__ (*args, **kwargs)

    class Meta:
        fields = ('name', 'description', 'author', 'create_on', 'last_change_on', 'part')
