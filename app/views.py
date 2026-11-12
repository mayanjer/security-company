from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def login_view(request):
    return render(request, 'login.html')

def index_view(request):
    return render(request, 'index.html')

def delete_instance(request, pk):
    return render(request, 'shift.html')

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

def delete_shift_view(request, pk):
    Shift.objects.get(pk =pk).delete()
    return redirect(shift_view)

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
    weapon = Weapon.objects.get(pk = pk)
    if request.method == "POST":
        form = WeaponForm(request.POST, instance = weapon)
        if form.is_valid():
            form.save()
            return redirect(weapon_view)
    else:
        form = WeaponForm(instance = weapon)
        context = {'form':form}
    return render(request, 'edit-weapon.html', context)

def delete_weapon_view(request, pk):
    Weapon.objects.get(pk =pk).delete()
    return redirect(delete_weapon_view)

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

def delete_client_organisation_view(request, pk):
    ClientOrganisation.objects.get(pk =pk).delete()
    return redirect(client_organisation_view)

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

def delete_client_payment_view(request, pk):
    ClientPayment.objects.get(pk =pk).delete()
    return redirect(client_payment_view)

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

def delete_company_branch_view(request, pk):
    CompanyBranch.objects.get(pk =pk).delete()
    return redirect(company_branch_view)

def deployment_view(request):
    if request.method == "POST":
        form = DeploymentForm(request.POST)
        if form.is_valid():
            form.save()
    form = DeploymentForm()
    deployments = Deployment.objects.all()
    context = {'form':form, 'deployments':deployments}
    return render(request, 'deployment.html', context)

def edit_deployment_view(request, pk):
    deployment = Deployment.objects.get(pk = pk)
    if request.method == "POST":
        form = DeploymentForm(request.POST, instance = deployment)
        if form.is_valid():
            form.save()
            return redirect(deployment_view)

    else:
        form = DeploymentForm(instance = deployment)
    context = {'form':form}
    return render(request, 'edit-deployment.html', context)

def delete_deployment_view(request, pk):
    Deployment.objects.get(pk =pk).delete()
    return redirect(deployment_view)

def guard_deployment_view(request):
    if request.method == "POST":
        form = GuardDeploymentForm(request.POST)
        if form.is_valid():
            form.save()
    form = GuardDeploymentForm()
    deployments = GuardDeployment.objects.all()
    context = {'form':form, 'deployments':deployments}
    return render(request, 'guard-deployment.html', context)

def edit_guard_deployment_view(request, pk):
    deployment = GuardDeployment.objects.get(pk = pk)
    if request.method == "POST":
        form = GuardDeploymentForm(request.POST, instance = deployment)
        if form.is_valid():
            form.save()
            return redirect(guard_deployment_view)
    else:
        form = GuardDeploymentForm(instance = deployment)

    context = {'form':form}
    return render(request, 'edit-guard-deployment.html', context)

def delete_guard_deployment_view(request, pk):
    GuardDeployment.objects.get(pk =pk).delete()
    return redirect(guard_deployment_view)

def guard_view(request):
    if request.method == "POST":
        form = GuardForm(request.POST)
        if form.is_valid():
            form.save()
    form = GuardForm()
    guards = Guard.objects.all()
    context = {'form':form, 'guards':guards}
    return render(request, 'guard.html', context)

def edit_guard_view(request, pk):
    guard = Guard.objects.get(pk = pk)
    if request.method == "POST":
        form = GuardForm(request.POST, instance = guard)
        if form.is_valid():
            form.save()
            return redirect(guard_view)

    else:
        form = GuardForm(instance = guard)
    context = {'form':form}
    return render(request, 'edit-guard.html', context)

def delete_guard_view(request, pk):
    Guard.objects.get(pk =pk).delete()
    return redirect(guard_view)

def guard_payment_view(request):
    if request.method == "POST":
        form = GuardPaymentForm(request.POST)
        if form.is_valid():
            form.save()
    form = GuardPaymentForm()
    payments = GuardPayment.objects.all()
    context = {'form':form, 'payments':payments}
    return render(request, 'guard-payment.html', context)

def edit_guard_payment_view(request, pk):
    payment = GuardPayment.objects.get(pk = pk)
    if request.method == 'POST':
        form = GuardPaymentForm(request.POST, instance = payment)
        if form.is_valid():
            form.save()
            return redirect(guard_payment_view)
    else:
        form = GuardPaymentForm(instance=payment)

    context = {'form':form}
    return render(request, 'edit-guard-payment.html', context)

def delete_guard_payment_view(request, pk):
    GuardPayment.objects.get(pk =pk).delete()
    return redirect(guard_payment_view)

def weapon_assignment_view(request):
    if request.method == "POST":
        form = WeaponAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
    form = WeaponAssignmentForm()
    assignemts = WeaponAssignment.objects.all() 
    context = {'form':form, 'assignments':assignemts}
    return render(request, 'weapon-assignment.html', context)

def edit_weapon_assignment(request, pk):
    assignment = WeaponAssignment.objects.get(pk = pk)
    if request.method == "POST":
        form = WeaponAssignmentForm(request.POST, instance = assignment)
        if form.is_valid():
            form.save()
            return redirect(weapon_assignment_view)
    else:
        form = WeaponAssignmentForm(instance = assignment)
    context = {'form':form}
    return render(request, 'edit-weapon-assignment.html', context)

def delete_weapon_assignmemt_view(request, pk):
    WeaponAssignment.objects.get(pk =pk).delete()
    return redirect(weapon_assignment_view)