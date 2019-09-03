from . import models
from django.forms import ModelForm

class NewPersonForm(ModelForm):
    class Meta:
        model = models.Person
        fields = ('name', 'presented')

class NewLabForm(ModelForm):
    class Meta:
        model = models.LabGroup
        fields = ('name',)
