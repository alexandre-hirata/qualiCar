from django import forms
from qualiCar_API.models import Vehicle, Part, Incident, UserProfile


class PartsForm (forms.Form):
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

    def __init__(self, *args, **kwargs):
        self.UserProfile = UserProfile

        super (PartsForm, self).__init__ (*args, **kwargs)

    class Meta:
        fields = ('name', 'description', 'author',)
