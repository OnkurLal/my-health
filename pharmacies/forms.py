from django.forms import ModelForm
from pharmacies.models import Pharmacy

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
