from django.contrib import admin
from pharmacies.models import Pharmacy

# Register your models here.
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
