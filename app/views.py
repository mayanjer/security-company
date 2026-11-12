from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .forms import *
from django.db.models import Sum

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Replace with your dashboard URL name
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html', {'form': form})

def sign_up_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically logs the user in after signing up
            return redirect('dashboard')  # Replace with your dashboard URL name
    else:
        form = UserCreationForm()
        
    return render(request, 'signup.html', {'form': form})

def index_view(request):
    return render(request, 'index.html')

def dashboard_view(request):
    # Weapon counts
    total_weapons = Weapon.objects.count()
    assigned_weapons = WeaponAssignment.objects.filter(assignment_status=True).count()
    available_weapons = max(total_weapons - assigned_weapons, 0)

    # Financial aggregations (defaulting to 0 if None)
    total_client_payable = ClientOrganisation.objects.filter(status=True).aggregate(
        total=Sum('amount_payable')
    )['total'] or 0

    total_client_paid = ClientPayment.objects.aggregate(
        total=Sum('amount_paid')
    )['total'] or 0

    total_guard_paid = GuardPayment.objects.aggregate(
        total=Sum('amount_paid')
    )['total'] or 0

    context = {
        # Guard metrics
        'active_guards': Guard.objects.filter(status=True).count(),
        'total_guards': Guard.objects.count(),

        # Client metrics
        'active_clients': ClientOrganisation.objects.filter(status=True).count(),
        'total_client_payable': total_client_payable,

        # Deployment metrics
        'active_deployments': Deployment.objects.filter(deployment_status=True).count(),
        'deployed_guards_count': GuardDeployment.objects.filter(deployment_status=True).count(),

        # Weapon metrics
        'total_weapons': total_weapons,
        'assigned_weapons': assigned_weapons,
        'available_weapons': available_weapons,

        # Branch & Shift metrics
        'active_branches': CompanyBranch.objects.filter(status=True).count(),
        'active_shifts': Shift.objects.filter(status=True).count(),

        # Payment metrics
        'total_client_paid': total_client_paid,
        'total_guard_paid': total_guard_paid,

        # Recent activity lists
        'recent_guard_deployments': GuardDeployment.objects.select_related(
            'guard', 'deployment__client_organisation', 'deployment__branch', 'deployment__shift'
        ).order_by('-date_deployed')[:5],

        'recent_weapon_assignments': WeaponAssignment.objects.select_related(
            'weapon', 'guard'
        ).order_by('-date_assigned')[:5],

        'recent_client_payments': ClientPayment.objects.select_related(
            'client_organisation'
        ).order_by('-date_paid')[:5],
    }
    return render(request, 'dashboard.html', context)

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