from django.urls import path
from medications.views import (
    create_medication,
    update_medication,
    delete_medication,
    med_info,
    med_indications,
    med_dosages,
    med_contraindications,
    med_boxed_warning,
    med_side_effects,
    drug_drug_interactions,
)


urlpatterns = [
    path("create/", create_medication, name="create_medication"),
    path("<int:id>/delete/", delete_medication, name="delete_medication"),
    path("<int:id>/update/", update_medication, name="update_medication"),
    path("<int:id>/med_info/", med_info, name="med_info"),
    path("<int:id>/med_info/indication/", med_indications, name="med_indications"),
    path("<int:id>/med_info/dosage/", med_dosages, name="med_dosages"),
    path(
        "<int:id>/med_info/contraindication/",
        med_contraindications,
        name="med_contraindications",
    ),
    path(
        "<int:id>/med_info/boxed_warning/", med_boxed_warning, name="med_boxed_warning"
    ),
    path("<int:id>/med_info/side_effects/", med_side_effects, name="med_side_effects"),
    path(
        "med_info/drug_drug_interactions/",
        drug_drug_interactions,
        name="drug_drug_interactions",
    ),
]
