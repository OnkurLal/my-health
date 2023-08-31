from django.forms import ModelForm
from records.models import PersonalDetail, Disease, Doctor, Pharmacy, Medication

class PersonalDetailForm(ModelForm):
    class Meta:
        model = PersonalDetail
        fields = (
            'height',
            'weight',
            'blood_pressure',
            'cholesterol',
        )

class DiseaseForm(ModelForm):
    class Meta:
        model = Disease
        fields = (
            'name',
        )

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = (
            'name',
            'phone_number',
            'street_address',
            'city',
            'state',
            'specialty',
        )

class PharmacyForm(ModelForm):
    class Meta:
        model = Pharmacy
        fields = (
            'name',
            'phone_number',
            'street_address',
            'city',
            'state',
        )

class MedicationForm(ModelForm):
    class Meta:
        model = Medication
        fields = (
            'name',
            'strength',
            'directions',
            'doctor',
            'condition_used_for',
            'pharmacy',
        )
