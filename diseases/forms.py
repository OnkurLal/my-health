from django.forms import ModelForm
from diseases.models import Disease


class DiseaseForm(ModelForm):
    class Meta:
        model = Disease
        fields = (
            'name',
        )
