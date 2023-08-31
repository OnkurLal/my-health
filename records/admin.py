from django.contrib import admin
from records.models import PersonalDetail, Disease, Doctor, Pharmacy, Medication

# Register your models here.
@admin.register(PersonalDetail)
class PersonalDetailAdmin(admin.ModelAdmin):
    list_display = [
        'height',
        'weight',
        'blood_pressure',
        'cholesterol',
    ]

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'phone_number',
        'street_address',
        'city',
        'state',
        'specialty',
        'patient',
    ]

@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'patient',
    ]

@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'phone_number',
        'street_address',
        'city',
        'state',
        'patient',
    ]

@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'strength',
        'directions',
        'used_for',
        'pharmacy',
        'patient',
    ]
