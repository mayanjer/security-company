from django.shortcuts import render, redirect
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
    shifts = Shift.objects.all()
    context = {'form':form, 'shifts':shifts}
    return render(request, 'shift.html', context)

def edit_shift_view(request, pk):
    shift = Shift.objects.get(pk = pk)
    if request.method == "POST":
        form = ShiftForm(request.POST, instance=shift)
        if form.is_valid():
            form.save()
            return redirect(shift_view)
    else:
        form = ShiftForm(instance = shift)
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

def edit_weapon_view(request, pk):
    return render(request, 'edit', context)

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

def edit_client_organisation_view(request, pk):
    organisation = ClientOrganisation.objects.get(pk = pk)

    if request.method == "POST":
        form = ClientOrganisationForm(request.POST, instance = organisation)
        if form.is_valid():
            form.save()
            return redirect(client_organisation_view)
    else:
        form = ClientOrganisationForm(instance = organisation)
    context = {'form':form}
    return render(request, 'edit-client-organisation.html', context)

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

def edit_client_payment(request, pk):
    payment = ClientPayment.objects.get(pk=pk)
    if request.method == "POST":
        form = ClientPaymentForm(request.POST, instance = payment)
        if form.is_valid():
            form.save()
            return redirect(client_payment_view)

    else:
        form = ClientPaymentForm(instance = payment)
    context = {'form':form}
    return render(request, 'edit-client-payment.html', context)

def company_branch_view(request):
    if request.method == "POST":
        form = CompanyBranchForm(request.POST)
        if form.is_valid():
            form.save()
    form = CompanyBranchForm()
    branches = CompanyBranch.objects.all()
    context = {'form':form, 'branches':branches}
    return render(request, 'company-branch.html', context)

def edit_company_branch_view(request, pk):
    branch = CompanyBranch.objects.get(pk = pk)
    if request.method == "POST":
        form = CompanyBranchForm(request.POST, instance = branch)
        if form.is_valid():
            form.save()
            return redirect(company_branch_view)
    else:
        form = CompanyBranchForm(instance = branch)
    context = {'form':form}
    return render(request, 'edit-company-branch.html', context)

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
    deployments = GuardDeployment.objects.all()
    context = {'form':form, 'deployments':deployments}
    return render(request, 'guard-deployment.html', context)

def guard_view(request):
    if request.method == "POST":
        form = GuardForm(request.POST)
        if form.is_valid():
            form.save()
    form = GuardForm()
    guards = Guard.objects.all()
    context = {'form':form, 'guards':guards}
    return render(request, 'guard.html', context)

def guard_payment_view(request):
    if request.method == "POST":
        form = GuardPaymentForm(request.POST)
        if form.is_valid():
            form.save()
    form = GuardPaymentForm()
    payments = GuardPayment.objects.all()
    context = {'form':form, 'payments':payments}
    return render(request, 'guard-payment.html', context)

def weapon_assignment_view(request):
    if request.method == "POST":
        form = WeaponAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
    form = WeaponAssignmentForm()
    assignemts = WeaponAssignment.objects.all() 
    context = {'form':form, 'assignments':assignemts}
    return render(request, 'weapon-assignment.html', context)