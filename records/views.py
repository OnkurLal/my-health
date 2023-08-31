from django.shortcuts import render, get_object_or_404, render
from records.models import PersonalDetail, Disease, Doctor, Pharmacy, Medication
from django.contrib.auth.decorators import login_required
from records.forms import PersonalDetailForm, DiseaseForm, DoctorForm, PharmacyForm, MedicationForm

# Create your views here.
def home(request):
    return render(request, 'records/home.html')

@login_required
def my_record(request):
    medications = get_object_or_404(Medication, patient = request.user)
    details = get_object_or_404(PersonalDetail, patient = request.user)
    doctors = get_object_or_404(Doctor, patient = request)
    diseases = get_object_or_404(Disease, patient = request)
    pharmacies = get_object_or_404(Pharmacy, patient = request)
    context = {
        'medications': medications,
        'details': details,
        'doctors': doctors,
        'diseases': diseases,
        'pharmacies': pharmacies,
    }
    return render(request, 'records/my_record.html', context)

# @login_required
# def create_details(request):
