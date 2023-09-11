from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from diseases.models import Disease
from diseases.forms import DiseaseForm


# Create your views here.
@login_required
def create_disease(request):
    if request.method == "POST":
        form = DiseaseForm(request.POST)
        if form.is_valid():
            disease = form.save(False)
            disease.patient = request.user
            disease.save()
            return redirect("my_record")
    else:
        form = DiseaseForm()
    context = {
        "form": form,
    }
    return render(request, "diseases/create.html", context)


@login_required
def update_disease(request, id):
    disease = get_object_or_404(Disease, id=id)
    if request.method == "POST":
        form = DiseaseForm(request.POST, instance=disease)
        if form.is_valid():
            form.save()
            return redirect("my_record")
    else:
        form = DiseaseForm(instance=disease)
    context = {
        "form": form,
        "disease": disease,
    }
    return render(request, "diseases/update.html", context)


def delete_disease(request, id):
    disease = get_object_or_404(Disease, id=id)
    if request.method == "POST":
        disease.delete()
        return redirect("my_record")
    context = {
        "disease": disease,
    }
    return render(request, "diseases/delete.html", context)
