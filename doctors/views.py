from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from doctors.models import Doctor
from doctors.forms import DoctorForm

# Create your views here.


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
        'doctor': doctor,
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
    return render(request, 'doctors/delete.html', context)
