from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Guard)
admin.site.register(ClientOrganisation)
admin.site.register(CompanyBranch)
admin.site.register(Shift)
admin.site.register(Weapon)
admin.site.register(ClientPayment)
admin.site.register(Deployment)
admin.site.register(GuardDeployment)
admin.site.register(GuardPayment)
admin.site.register(WeaponAssignment)

