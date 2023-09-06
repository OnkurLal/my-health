from django.shortcuts import render, get_object_or_404, redirect
from records.models import PersonalDetail, Medication
from django.contrib.auth.decorators import login_required
from records.forms import PersonalDetailForm, MedicationForm
import requests

# Create your views here.
def home(request):
    return render(request, 'records/home.html')

@login_required
def my_record(request):
    return render(request, 'records/my_record.html',)

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
    response = requests.get(f'https://api.fda.gov/drug/label.json?search=description:{medication.name}')
    response_data = response.json()
    print(response_data['results'][0])
    data = response_data['results'][0]
    context = {
        'medication': medication,
        'data': data
    }
    return render(request, 'medication/med_info.html',context)
