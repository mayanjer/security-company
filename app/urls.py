from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name = 'login'),
   
    path('', index_view, name='index'),

    path('client_organisation/', client_organisation_view, name = "client-organisation"),
    path('edit-client-organisation/<int:pk>', edit_client_organisation_view, name = "edit-client-organisation"),

    path('client_payment/', client_payment_view, name = "client-payment"),
    path('edit_client_payment/<int:pk>', edit_client_payment, name = 'edit-client-payment'),

    path('company_branch/', company_branch_view, name = 'company-branch'),
    path('edit_company_branch/<int:pk>', edit_company_branch_view, name = "edit-company-branch"),

    path('deployment/', deployment_view, name = "deployment"),
    path('edit_deployment/<int:pk>', edit_deployment_view, name = 'edit-deployment'),

    path('guard_deployment/', guard_deployment_view, name = 'guard-deployment'),
    path('edit_guard_deployment/<int:pk>', edit_guard_deployment_view, name= 'edit-guard-deployment'),


    path('guard/', guard_view, name = 'guard'),
    path('weapon/', weapon_view, name='weapon'),
    path('weapon_assignment/', weapon_assignment_view, name = 'weapon-assignment'),

     path('shift/', shift_view, name = 'shift'),
     path('edit-shift/<int:pk>', edit_shift_view, name = "edit-shift"),

     path('guard_payment/', guard_payment_view, name = 'guard-payment')
   
]