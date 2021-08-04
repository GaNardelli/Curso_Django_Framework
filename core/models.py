from django.db import models

class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    price = models.DecimalField('Price',decimal_places=2, max_digits=9)
    storage = models.IntegerField("Quantity in storage")
    objects = models.Manager()

    def __str__(self):
        return self.name
    


class Client(models.Model):
    name = models.CharField("First Name", max_length=100)
    lastName = models.CharField("Last Name", max_length=100)
    email = models.EmailField("Email", max_length=100)
    objects = models.Manager()

    def __str__(self):
        return f'{self.name} {self.lastName}'
    