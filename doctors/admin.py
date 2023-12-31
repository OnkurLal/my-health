from django.contrib import admin
from doctors.models import Doctor

# Register your models here.


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "phone_number",
        "street_address",
        "city",
        "state",
        "specialty",
        "patient",
    ]
