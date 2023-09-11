from django.forms import ModelForm
from medications.models import Medication


class MedicationForm(ModelForm):
    class Meta:
        model = Medication
        fields = (
            "name",
            "strength",
            "directions",
            "doctor",
            "condition_used_for",
            "pharmacy",
        )
