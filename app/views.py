from django.shortcuts import render
from .forms import *

# Create your views here.
def login_view(request):
    return render(request, 'login.html')

def index_view(request):
    return render(request, 'index.html')

def shift_view(request):
    form = ShiftForm()
    context = {'form':form}
    return render(request, 'shift.html', context)

def weapon_view(request):
    form = WeaponForm()
    context = {'form':form}
    return render(request, 'weapon.html', context)

def client_organisation_view(request):
    form = ClientOrganisationForm()
    context = {
        'form': form
        }
    return render(request, 'client-organisation.html', context)

def client_payment_view(request):
    form = ClientPaymentForm()
    context = {'form':form}
    return render(request, 'client-payment.html', context)

def company_branch_view(request):
    form = CompanyBranchForm()
    context = {'form':form}
    return render(request, 'company-branch.html', context)

def deployment_view(request):
    form = DeploymentForm()
    context = {'form':form}
    return render(request, 'deployment.html', context)

def guard_deployment_view(request):
    form = GuardDeploymentForm()
    context = {'form':form}
    return render(request, 'guard-deployment.html', context)

def guard_view(request):
    form = GuardForm()
    context = {'form':form}
    return render(request, 'guard.html', context)

def guard_payment_view(request):
    form = GuardPaymentForm()
    context = {'form':form}
    return render(request, 'guard-payment.html', context)

def weapon_assignment_view(request):
    form = WeaponAssignmentForm()
    context = {'form':form}
    return render(request, 'weapon-assignment.html', context)