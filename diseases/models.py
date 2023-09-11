from django.db import models
from django.conf import settings

# Create your models here.


class Disease(models.Model):
    name = models.CharField(max_length=100)
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='diseases',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
