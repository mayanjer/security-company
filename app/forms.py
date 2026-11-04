from django import forms
from .models import *

class ClientOrganisationForm(forms.Form):
    class Meta:
        model = ClientOrganisation
        fields = "__all__"