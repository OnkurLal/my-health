from django.shortcuts import render, get_object_or_404, render
from records.models import PersonalDetail, Disease, Doctor, Pharmacy, Medication
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def my_record(request):
    medications = get_object_or_404(Medication, patient = request.user)
    context = {
        'medications': medications,
    }
    return render(request, 'records/my_record.html', context)
