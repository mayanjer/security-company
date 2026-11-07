from django.shortcuts import render
from .forms import *

# Create your views here.
def login_view(request):
    return render(request, 'login.html')

def index_view(request):
    return render(request, 'index.html')

def shift_view(request):
    if request.method == "POST":
        print(request.POST)
        form = ShiftForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("failed")
    form = ShiftForm()
    context = {'form':form}
    return render(request, 'shift.html', context)

def weapon_view(request):
    if request.method == "POST":
        form = WeaponForm(request.POST)
        if form.is_valid():
            form.save()
    form = WeaponForm()
    weapons = Weapon.objects.all()
    context = {'form':form, 'weapons':weapons}
    return render(request, 'weapon.html', context)

def client_organisation_view(request):
    if request.method == "POST":
        form = ClientOrganisationForm(request.POST)
        if form.is_valid():
            form.save()
    form = ClientOrganisationForm()
    organisations = ClientOrganisation.objects.all()
    context = {
        'form': form,
        'organisations':organisations
        }
    return render(request, 'client-organisation.html', context)

def client_payment_view(request):
    if request.method == "POST":
        form = ClientPaymentForm(request.POST)
        if form.is_valid():
            form.save()

    form = ClientPaymentForm()
    payments = ClientPayment.objects.all()
    context = {'form':form,
               'payments':payments}
    return render(request, 'client-payment.html', context)

def company_branch_view(request):
    if request.method == "POST":
        form = CompanyBranchForm(request.POST)
        if form.is_valid():
            form.save()
    form = CompanyBranchForm()
    branches = CompanyBranch.objects.all()
    context = {'form':form, 'branches':branches}
    return render(request, 'company-branch.html', context)

def deployment_view(request):
    if request.method == "POST":
        form = DeploymentForm(request.POST)
        if form.is_valid():
            form.save()
    form = DeploymentForm()
    deployments = Deployment.objects.all()
    context = {'form':form, 'deployments':deployments}
    return render(request, 'deployment.html', context)

def guard_deployment_view(request):
    if request.method == "POST":
        form = GuardDeploymentForm(request.POST)
        if form.is_valid():
            form.save()
    form = GuardDeploymentForm()
    context = {'form':form}
    return render(request, 'guard-deployment.html', context)

def guard_view(request):
    if request.method == "POST":
        form = GuardForm(request.POST)
        if form.is_valid():
            form.save()
    form = GuardForm()
    context = {'form':form}
    return render(request, 'guard.html', context)

def guard_payment_view(request):
    if request.method == "POST":
        form = GuardPaymentForm(request.POST)
        if form.is_valid():
            form.save()
    form = GuardPaymentForm()
    context = {'form':form}
    return render(request, 'guard-payment.html', context)

def weapon_assignment_view(request):
    if request.method == "POST":
        form = WeaponAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
    form = WeaponAssignmentForm()
    context = {'form':form}
    return render(request, 'weapon-assignment.html', context)