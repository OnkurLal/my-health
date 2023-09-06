from django.contrib import admin
from records.models import PersonalDetail

# Register your models here.
@admin.register(PersonalDetail)
class PersonalDetailAdmin(admin.ModelAdmin):
    list_display = [
        'height',
        'weight',
        'blood_pressure',
        'cholesterol',
    ]
