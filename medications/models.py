from django.db import models
from django.conf import settings
from diseases.models import Disease
from doctors.models import Doctor
from pharmacies.models import Pharmacy

# Create your models here.


class Medication(models.Model):
    name = models.CharField(max_length=100)
    strength = models.CharField(max_length=20)
    directions = models.TextField()
    doctor = models.ForeignKey(
        Doctor,
        related_name="medications",
        on_delete=models.CASCADE,
    )
    condition_used_for = models.ForeignKey(
        Disease,
        related_name="medications",
        on_delete=models.CASCADE,
    )
    pharmacy = models.ForeignKey(
        Pharmacy,
        related_name="medications",
        on_delete=models.CASCADE,
    )
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="medications",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
