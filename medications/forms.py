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

    def __init__(self, user, *args, **kwargs):
        super(MedicationForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].queryset = user.doctors.all()
        self.fields['pharmacy'].queryset = user.pharmacies.all()
        self.fields['condition_used_for'].queryset = user.diseases.all()
