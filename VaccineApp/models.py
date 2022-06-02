from django.db import models


# Create your models here.

class Human(models.Model):
    HumanId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    dateOfBirth = models.DateField()
    address = models.CharField(max_length=100)
    City = models.CharField(max_length=50)
    zipCode = models.PositiveIntegerField(null=True)
    landLine = models.CharField(max_length=100)
    cellularPhone = models.CharField(max_length=20)
    infected = models.BooleanField()
    conditions = models.CharField(max_length=1000, blank=True)
