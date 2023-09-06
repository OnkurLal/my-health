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
