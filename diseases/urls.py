from django.urls import path
from diseases.views import create_disease, update_disease, delete_disease

urlpatterns = [
    path('create/', create_disease, name='create_disease'),
    path('<int:id>/update/', update_disease, name='update_disease'),
    path('<int:id>/delete/', delete_disease, name='delete_disease'),
]
