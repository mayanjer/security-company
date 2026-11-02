from django.db import models

# Create your models here.
class ClientOrganisation(models.Model):
    client_name = models.CharsField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    location = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    organisation_email = models.EmailField(max_length=100, unique=True)
    branch = models.CharField(max_length=100)
    amount_payable = models.DecimalField(max_digits=10, decimal_places=2)

class ClientPayment(models.Model):
    client_organisation = models.ForeignKey(ClientOrganisation, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField()
    paymnet_method = models.CharField(max_length=50)
    month = models.CharField(max_length=20)
    year = models.CharField(max_length=4)

class CompanyBranch(models.Model):
    branch_name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    locatiion = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    branch_email = models.EmailField(max_length=100, unique=True)