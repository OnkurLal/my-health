from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from medications.models import Medication
from medications.forms import MedicationForm
import requests

# Create your views here.
@login_required
def create_medication(request):
    if request.method == 'POST':
        form = MedicationForm(request.POST)
        if form.is_valid():
            medication = form.save(False)
            medication.patient = request.user
            medication.save()
            return redirect('my_record')
    else:
        form = MedicationForm()
    context = {
        'form': form,
    }
    return render(request, 'medication/create.html', context)

@login_required
def update_medication(request, id):
    medication = get_object_or_404(Medication, id=id)
    if request.method == 'POST':
        form = MedicationForm(request.POST, instance=medication)
        if form.is_valid():
            form.save()
            return redirect('my_record')
    else:
        form = MedicationForm(instance=medication)
    context = {
        'form': form,
        'medication': medication,
    }
    return render(request, 'medication/update.html', context)

@login_required
def delete_medication(request, id):
    medication = get_object_or_404(Medication, id=id)
    if request.method == 'POST':
        medication.delete()
        return redirect('my_record')
    context = {
        'medication': medication,
    }
    return render(request, 'medication/delete.html',context)

def med_info(request,id):
    medication = get_object_or_404(Medication, id=id)
    context = {
        'medication': medication,
    }
    return render(request, 'information/med_info.html',context)

def med_indications(request, id):
    medication = get_object_or_404(Medication, id=id)
    try:
        response = requests.get(f'https://api.fda.gov/drug/label.json?search=description:{medication.name}')
        response_data = response.json()
        indication = response_data['results'][0]['indications_and_usage'][0]
    except:
        indication = 'Please make sure the drug name is spelled correctly or this data might not be available.'

    context = {
        'medication': medication,
        'indication': indication
    }
    return render(request, 'information/indication.html',context)

def med_dosages(request, id):
    medication = get_object_or_404(Medication, id=id)
    try:
        response = requests.get(f'https://api.fda.gov/drug/label.json?search=description:{medication.name}')
        response_data = response.json()
        dosage = response_data['results'][0]['dosage_and_administration'][0]
    except:
        dosage = 'Please make sure the drug name is spelled correctly or this data might not be available.'

    context = {
        'medication': medication,
        'dosage': dosage,
    }
    return render(request, 'information/dosage.html',context)

def med_contraindications(request, id):
    medication = get_object_or_404(Medication, id=id)
    try:
        response = requests.get(f'https://api.fda.gov/drug/label.json?search=description:{medication.name}')
        response_data = response.json()
        contraindications = response_data['results'][0]['contraindications'][0]
    except:
        contraindications = 'Please make sure the drug name is spelled correctly or this data might not be available.'

    context = {
        'medication': medication,
        'contraindications': contraindications,
    }
    return render(request, 'information/contraindications.html',context)

def med_boxed_warning(request, id):
    medication = get_object_or_404(Medication, id=id)
    try:
        response = requests.get(f'https://api.fda.gov/drug/label.json?search=description:{medication.name}')
        response_data = response.json()
        boxed_warning = response_data['results'][0]['boxed_warning'][0]
    except:
        boxed_warning = 'Please make sure the drug name is spelled correctly or this data might not be available.'

    context = {
        'medication': medication,
        'boxed_warning': boxed_warning,
    }
    return render(request, 'information/boxed_warning.html',context)

def med_side_effects(request, id):
    medication = get_object_or_404(Medication, id=id)
    try:
        response = requests.get(f'https://api.fda.gov/drug/label.json?search=description:{medication.name}')
        response_data = response.json()
        side_effects = response_data['results'][0]['adverse_reactions'][0]
    except:
        side_effects = 'Please make sure the drug name is spelled correctly or this data might not be available.'

    context = {
        'medication': medication,
        'side_effects': side_effects,
    }
    return render(request, 'information/side_effects.html',context)
