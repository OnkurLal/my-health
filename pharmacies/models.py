from django.db import models
from django.conf import settings


# Create your models here.
class Pharmacy(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5, null=True)
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="pharmacies",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
