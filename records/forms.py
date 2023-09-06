from django.forms import ModelForm
from records.models import PersonalDetail, Medication

class PersonalDetailForm(ModelForm):
    class Meta:
        model = PersonalDetail
        fields = (
            'height',
            'weight',
            'blood_pressure',
            'cholesterol',
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
