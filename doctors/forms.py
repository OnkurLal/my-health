from django.forms import ModelForm
from doctors.models import Doctor


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
