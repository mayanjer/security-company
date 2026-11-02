from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def client_organisation(request):
    return render(request, 'client-organisation.html')