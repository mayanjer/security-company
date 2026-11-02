from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def client_organisation(request):
    return render(request, 'client-organisation.html')

def client_payment(request):
    return render(request, 'client_payment.html')

def company_branch(request):
    return render(request, 'company-branch.html')

def deployment(request):
    return render(request, 'deployment.html')

def guard_deployment(request):
    return render(request, 'guard-deployment.html')

def guard(request):
    return render(request, 'guard.html')