from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    address1 = models.CharField(max_length=100, default="")
    address2 = models.CharField(max_length=50, blank=True, default="")
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=60)
    zipcode = models.CharField(max_length=20, default="")
    email = models.EmailField(max_length=254, unique=True)
    phone = PhoneNumberField(blank=False, region='US', unique=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
