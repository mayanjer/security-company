from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('client_organisation/', client_organisation, name = "client-organisation")
]
