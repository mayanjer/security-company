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

class CompanyBranchForm(forms.ModelForm):
    class Meta:
        model = CompanyBranch
        fields = "__all__"

class DeploymentForm(forms.ModelForm):
    class Meta:
        model = Deployment
        fields = "__all__"

class GuardPaymentForm(forms.ModelForm):
    class Meta:
        model = GuardPayment
        fields = "__all__"

class GuardDeploymentForm(forms.ModelForm):
    class Meta:
        model = GuardDeployment
        fields = "__all__"

class GuardForm(forms.ModelForm):
    class Meta:
        model = Guard
        fields = "__all__"

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = "__all__"

class WweaponAssignmentForm(forms.ModelForm):
    class Meta:
        model = WeaponAssignment
        fields = "__all__"

class WeaponForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = "__all__"


