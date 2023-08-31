from django.db import models
from django.conf import settings
# Create your models here.

class PersonalDetail(models.Model):
    height = models.CharField(max_length=20)
    weight = models.PositiveSmallIntegerField()
    blood_pressure = models.CharField(max_length=10)
    cholesterol = models.PositiveSmallIntegerField()
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='details',
        on_delete=models.CASCADE,
    )

class Disease(models.Model):
    name = models.CharField(max_length=100)
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='diseases',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=15)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    specialty = models.CharField(max_length=100)
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='doctors',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

class Pharmacy(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='pharmacies',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

class Medication(models.Model):
    name = models.CharField(max_length=100)
    strength = models.CharField(max_length=20)
    directions = models.TextField()
    doctor = models.ForeignKey(
        Doctor,
        related_name='medications',
        on_delete=models.CASCADE,
    )
    condition_used_for = models.ForeignKey(
        Disease,
        related_name='medications',
        on_delete=models.CASCADE,
    )
    pharmacy = models.ForeignKey(
        Pharmacy,
        related_name='medications',
        on_delete=models.CASCADE,
    )
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='medications',
        on_delete=models.CASCADE,
    )

def __str__(self):
    return self.nme
