from django.contrib import admin
from records.models import PersonalDetail, Medication

# Register your models here.
@admin.register(PersonalDetail)
class PersonalDetailAdmin(admin.ModelAdmin):
    list_display = [
        'height',
        'weight',
        'blood_pressure',
        'cholesterol',
    ]

@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'strength',
        'directions',
        'condition_used_for',
        'pharmacy',
        'patient',
    ]
