from django.shortcuts import render, get_object_or_404, redirect
from records.models import PersonalDetail
from django.contrib.auth.decorators import login_required
from records.forms import PersonalDetailForm

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
