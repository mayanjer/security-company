from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name = 'login'),
   
    path('', index_view, name='index'),

    path('client_organisation/', client_organisation_view, name = "client-organisation"),
    path('edit-client-organisation/<int:pk>', edit_client_organisation_view, name = "edit-client-organisation"),
     path('delete_client_organisation/<int:pk>', delete_client_organisation_view, name = 'delete-client-organisation'),

    path('client_payment/', client_payment_view, name = "client-payment"),
    path('edit_client_payment/<int:pk>', edit_client_payment, name = 'edit-client-payment'),
     path('delete_client_payment/<int:pk>', delete_client_payment_view, name = 'delete-client-payment'),

    path('company_branch/', company_branch_view, name = 'company-branch'),
    path('edit_company_branch/<int:pk>', edit_company_branch_view, name = "edit-company-branch"),
     path('delete_company_branch/<int:pk>', delete_company_branch_view, name = 'delete-company-branch'),

    path('deployment/', deployment_view, name = "deployment"),
    path('edit_deployment/<int:pk>', edit_deployment_view, name = 'edit-deployment'),
     path('delete_deployment/<int:pk>', delete_deployment_view, name = 'delete-deployment'),

    path('guard_deployment/', guard_deployment_view, name = 'guard-deployment'),
    path('edit_guard_deployment/<int:pk>', edit_guard_deployment_view, name= 'edit-guard-deployment'),
     path('delete_guard_deployment/<int:pk>', delete_guard_deployment_view, name = 'delete-guard-deployment'),


    path('guard/', guard_view, name = 'guard'),
    path('edit-guard/<int:pk>', edit_guard_view, name = 'edit-guard'),
     path('delete_guard/<int:pk>', delete_guard_view, name = 'delete-guard'),

    path('weapon/', weapon_view, name='weapon'),
    path('edit_weapon/<int:pk>', edit_weapon_view, name = 'edit-weapon'),
     path('delete_weapon/<int:pk>', delete_weapon_view, name = 'delete-weapon'),

    path('weapon_assignment/', weapon_assignment_view, name = 'weapon-assignment'),
    path('edit-weapon-assignment/<int:pk>', edit_weapon_assignment, name = 'edit-weapon-assignment'),
     path('delete_weapon_assignment/<int:pk>', delete_weapon_assignmemt_view, name = 'delete-weapon-assignment'),

     path('shift/', shift_view, name = 'shift'),
     path('edit-shift/<int:pk>', edit_shift_view, name = "edit-shift"),
     path('delete_shift/<int:pk>', delete_shift_view, name = 'delete-shift'),

     path('guard_payment/', guard_payment_view, name = 'guard-payment'),
     path('edit_guard_payment/<int:pk>', edit_guard_payment_view, name = 'edit-guard-payment'),
     path('delete_guard_payment/<int:pk>', delete_guard_payment_view, name = 'delete-guard_payment'),
     
]