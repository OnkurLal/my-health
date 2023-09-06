from django.forms import ModelForm
from records.models import PersonalDetail

class PersonalDetailForm(ModelForm):
    class Meta:
        model = PersonalDetail
        fields = (
            'height',
            'weight',
            'blood_pressure',
            'cholesterol',
        )
