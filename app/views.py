from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'login.html')

def index_view(request):
    return render(request, 'index.html')

def shift_view(request):
    return render(request, 'shift.html')

def weapon_view(request):
    return render(request, 'weapon.html')

def client_organisation_view(request):
    return render(request, 'client-organisation.html')

def client_payment_view(request):
    return render(request, 'client-payment.html')

def company_branch_view(request):
    return render(request, 'company-branch.html')

def deployment_view(request):
    return render(request, 'deployment.html')

def guard_deployment_view(request):
    return render(request, 'guard-deployment.html')

def guard_view(request):
    return render(request, 'guard.html')

def guard_payment_view(request):
    return render(request, 'guard-payment.html')

def weapon_assignment_view(request):
    return render(request, 'weapon-assignment.html')