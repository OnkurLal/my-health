from django.urls import path
from doctors.views import create_doctor, update_doctor, delete_doctor

urlpatterns = [
    path('create/', create_doctor, name='create_doctor'),
    path('<int:id>/delete/', delete_doctor, name='delete_doctor'),
    path('<int:id>/update/', update_doctor, name='update_doctor'),
]
