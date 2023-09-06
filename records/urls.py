from django.urls import path
from records.views import my_record, home, create_details, update_details, create_medication, update_medication, delete_medication, med_info

urlpatterns =[
    path('', home, name='home'),
    path('my_record/', my_record, name='my_record'),
    path('details/create/', create_details, name='create_details'),
    path('details/<int:id>/update/', update_details, name='update_details'),
    path('medication/create/', create_medication, name='create_medication'),
    path('medication/<int:id>/delete/', delete_medication, name='delete_medication'),
    path('medication/<int:id>/update/', update_medication, name='update_medication'),
    path('medication/<int:id>/med_info/', med_info, name='med_info'),
]
