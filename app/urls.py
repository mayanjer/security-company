from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('client_organisation/', client_organisation, name = "client-organisation"),
    path('client_payment/', client_payment, name = "client-payment"),
    path('company_branch/', company_branch, name = 'company-branch'),
    path('deployment/', deployment, name = "deployment"),
    path('guard_deployment/', guard_deployment, name = 'guard-deployment'),
    path('guard/', guard, name = 'guard')
]
