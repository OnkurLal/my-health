from django.contrib import admin
from diseases.models import Disease

# Register your models here.


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'patient',
    ]
