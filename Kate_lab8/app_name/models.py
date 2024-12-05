from django.db import models

class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15)
    bank_account = models.CharField(max_length=20)

    def __str__(self):
        return self.company_name


class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    material_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.material_name


class Supply(models.Model):
    supply_id = models.AutoField(primary_key=True)
    supply_date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    delivery_days = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"Supply #{self.supply_id}"
