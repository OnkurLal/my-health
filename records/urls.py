from django.urls import path
from records.views import my_record, home, create_details, update_details, create_disease, update_disease,delete_disease, create_doctor, update_doctor, delete_doctor, create_pharmacy, update_pharmacy, delete_pharmacy

urlpatterns =[
    path('', home, name='home'),
    path('my_record/', my_record, name='my_record'),
    path('details/create', create_details, name='create_details'),
    path('details/<int:id>/update', update_details, name='update_details'),
    path('diseases/create', create_disease, name='create_disease'),
    path('diseases/<int:id>/update', update_disease, name='update_disease'),
    path('diseases/<int:id>/delete', delete_disease, name='delete_disease'),
    path('doctors/create', create_doctor, name='create_doctor'),
    path('doctors/<int:id>/delete', delete_doctor, name='delete_doctor'),
    path('doctors/<int:id>/update', update_doctor, name='update_doctor'),
    path('pharmacy/create', create_pharmacy, name='create_pharmacy'),
    path('pharmacy/<int:id>/delete', delete_pharmacy, name='delete_pharmacy'),
    path('pharmacy/<int:id>/update', update_pharmacy, name='update_pharmacy'),
]
