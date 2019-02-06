from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    producent = models.CharField(max_length=70)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()

    def __str__(self):
        return self.title


class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    dateOfPurchase = models.DateField(null=True, blank=True)
    paymentDate = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.client.email+" "+str(self.dateOfPurchase)


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Address(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=70, null=True, blank=True)
    firstName = models.CharField(max_length=70)
    surname = models.CharField(max_length=70)
    street = models.CharField(max_length=70)
    houseNumber = models.IntegerField()
    apartmentNumber = models.IntegerField(null=True, blank=True)
    zipCode = models.CharField(max_length=6)
    city = models.CharField(max_length=70)

    def __str__(self):
        return self.firstName+" "+self.surname+" "+self.city+" "+self.street
