from django import forms
from qualiCar_API.models import Vehicle, Part, Incident


class PartsForm (forms.Form):
    part = Part.objects.all ()
    # part = forms.ChoiceField (
    #     choices = Part.objects.all (),
    #     label='Parts',
    #     # widget=forms.Select (
    #     #     attrs = {'class' : 'form-control'}
    #     # )
    # )

    class Meta:
        fields = ('name', 'description', 'author',)
