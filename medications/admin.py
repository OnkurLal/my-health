from django.contrib import admin
from medications.models import Medication

# Register your models here.


@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "strength",
        "directions",
        "condition_used_for",
        "pharmacy",
        "patient",
    ]
