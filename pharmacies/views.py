from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from pharmacies.models import Pharmacy
from pharmacies.forms import PharmacyForm

# Create your views here.


@login_required
def create_pharmacy(request):
    if request.method == "POST":
        form = PharmacyForm(request.POST)
        if form.is_valid():
            pharmacy = form.save(False)
            pharmacy.patient = request.user
            pharmacy.save()
            return redirect("my_record")
    else:
        form = PharmacyForm()
    context = {
        "form": form,
    }
    return render(request, "pharmacy/create.html", context)


@login_required
def update_pharmacy(request, id):
    pharmacy = get_object_or_404(Pharmacy, id=id)
    if request.method == "POST":
        form = PharmacyForm(request.POST, instance=pharmacy)
        if form.is_valid():
            form.save()
            return redirect("my_record")
    else:
        form = PharmacyForm(instance=pharmacy)
    context = {
        "form": form,
        "pharmacy": pharmacy,
    }
    return render(request, "pharmacy/update.html", context)


def delete_pharmacy(request, id):
    pharmacy = get_object_or_404(Pharmacy, id=id)
    if request.method == "POST":
        pharmacy.delete()
        return redirect("my_record")
    context = {
        "pharmacy": pharmacy,
    }
    return render(request, "pharmacy/delete.html", context)
