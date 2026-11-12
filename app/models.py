from django.db import models

# Create your models here.
class ClientOrganisation(models.Model):
    client_name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    location = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    organisation_email = models.EmailField(max_length=100, unique=True)
    branch = models.CharField(max_length=100)
    amount_payable = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.client_name

class CompanyBranch(models.Model):
    branch_name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    location = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    branch_email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
            return self.branch_name

class Guard(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    status = models.BooleanField(default=True)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    date_joined = models.DateField(auto_now_add=True)
    def __str__(self):
            return f"{self.first_name} {self.last_name}"

class Shift(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.BooleanField(default=True)
    def __str__(self):
            return self.name

class Weapon(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=50)
    def __str__(self):
            return self.weapon
  

class ClientPayment(models.Model):
    client_organisation = models.ForeignKey(ClientOrganisation, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField()
    payment_method = models.CharField(max_length=50)
    month = models.CharField(max_length=20)
    year = models.CharField(max_length=4)
    def __str__(self):
            return self.client_organisation

class Deployment(models.Model):
    client_organisation = models.ForeignKey(ClientOrganisation, on_delete=models.CASCADE)
    branch = models.ForeignKey(CompanyBranch, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    deployment_status = models.BooleanField(default=True)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    def __str__(self):
            return f"{self.client_organisation} - {self.branch}"

class GuardDeployment(models.Model):
    guard = models.ForeignKey(Guard, on_delete=models.CASCADE)
    deployment = models.ForeignKey(Deployment, on_delete=models.CASCADE)
    date_deployed = models.DateField(auto_now_add=True)
    deployment_status = models.BooleanField(default=True)
    def __str__(self):
            return f"{self.guard} - {self.deployment}"

class GuardPayment(models.Model):
    guard = models.ForeignKey(Guard, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField()
    payment_method = models.CharField(max_length=50)
    month = models.CharField(max_length=20)
    year = models.CharField(max_length=4)
    def __str__(self):
            return self.guard

class WeaponAssignment(models.Model):
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    guard = models.ForeignKey(Guard, on_delete=models.CASCADE)
    date_assigned = models.DateField(auto_now_add=True)
    assignment_status = models.BooleanField(default=True)
    return_date = models.DateField(null=True, blank=True)
    def __str__(self):
            return f"{self.guard} - {self.weapon}"




