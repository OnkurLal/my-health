from django.shortcuts import render, get_object_or_404, redirect
from records.models import PersonalDetail, Disease, Doctor, Pharmacy, Medication
from django.contrib.auth.decorators import login_required
from records.forms import PersonalDetailForm, DiseaseForm, DoctorForm, PharmacyForm, MedicationForm

# Create your views here.
def home(request):
    return render(request, 'records/home.html')

@login_required
def my_record(request):
    medications = Medication.objects.filter(patient=request.user)
    doctors = Doctor.objects.filter(patient=request.user)
    diseases = Disease.objects.filter(patient=request.user)
    pharmacies = Pharmacy.objects.filter(patient=request.user)
    context = {
        'medications': medications,
        'doctors': doctors,
        'diseases': diseases,
        'pharmacies': pharmacies,
    }
    return render(request, 'records/my_record.html', context)

@login_required
def create_details(request):
    if request.method == 'POST':
        form = PersonalDetailForm(request.POST)
        if form.is_valid():
            details = form.save(False)
            details.patient = request.user
            details.save()
            return redirect('my_record')
    else:
        form = PersonalDetailForm()
    context = {
        'form': form,
    }
    return render(request, 'details/create.html', context)

@login_required
def update_details(request, id):
    details = get_object_or_404(PersonalDetail, id=id)
    if request.method == 'POST':
        form = PersonalDetailForm(request.POST, instance=details)
        if form.is_valid():
            form.save()
            return redirect('my_record')
    else:
        form = PersonalDetailForm(instance=details)
    context = {
        'form': form,
    }
    return render(request, 'details/update.html', context)

@login_required
def create_disease(request):
    if request.method == 'POST':
        form = DiseaseForm(request.POST)
        if form.is_valid():
            disease = form.save(False)
            disease.patient = request.user
            disease.save()
            return redirect('my_record')
    else:
        form = DiseaseForm()
    context = {
        'form': form,
    }
    return render(request, 'diseases/create.html', context)

@login_required
def update_disease(request, id):
    disease = get_object_or_404(Disease, id=id)
    if request.method == 'POST':
        form = DiseaseForm(request.POST, instance=disease)
        if form.is_valid():
            form.save()
            return redirect('my_record')
    else:
        form = DiseaseForm(instance=disease)
    context = {
        'form': form,
    }
    return render(request, 'diseases/update.html', context)

def delete_disease(request, id):
    disease = get_object_or_404(Disease, id=id)
    if request.method == 'POST':
        disease.delete()
        return redirect('my_record')
    context = {
        'disease': disease,
    }
    return render(request, 'diseases/delete.html',context)

@login_required
def create_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(False)
            doctor.patient = request.user
            doctor.save()
            return redirect('my_record')
    else:
        form = DoctorForm()
    context = {
        'form': form,
    }
    return render(request, 'doctors/create.html', context)

@login_required
def update_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('my_record')
    else:
        form = DoctorForm(instance=doctor)
    context = {
        'form': form,
    }
    return render(request, 'doctors/update.html', context)

def delete_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    if request.method == 'POST':
        doctor.delete()
        return redirect('my_record')
    context = {
        'doctor': doctor,
    }
    return render(request, 'doctors/delete.html',context)

@login_required
def create_pharmacy(request):
    if request.method == 'POST':
        form = PharmacyForm(request.POST)
        if form.is_valid():
            pharmacy = form.save(False)
            pharmacy.patient = request.user
            pharmacy.save()
            return redirect('my_record')
    else:
        form = PharmacyForm()
    context = {
        'form': form,
    }
    return render(request, 'pharmacy/create.html', context)

@login_required
def update_pharmacy(request, id):
    pharmacy = get_object_or_404(Pharmacy, id=id)
    if request.method == 'POST':
        form = PharmacyForm(request.POST, instance=pharmacy)
        if form.is_valid():
            form.save()
            return redirect('my_record')
    else:
        form = PharmacyForm(instance=pharmacy)
    context = {
        'form': form,
    }
    return render(request, 'pharmacy/update.html', context)

def delete_pharmacy(request, id):
    pharmacy = get_object_or_404(Pharmacy, id=id)
    if request.method == 'POST':
        pharmacy.delete()
        return redirect('my_record')
    context = {
        'pharmacy': pharmacy,
    }
    return render(request, 'pharmacy/delete.html',context)
