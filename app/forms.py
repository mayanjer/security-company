from django import forms
from .models import *

class ClientOrganisationForm(forms.ModelForm):
    class Meta:
        model = ClientOrganisation
        fields = "__all__"

class ClientPaymentForm(forms.ModelForm):
    class Meta:
        model = ClientPayment
        fields = "__all__"