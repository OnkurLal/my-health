from django.urls import path
from records.views import my_record, home, create_details, update_details, create_disease, update_disease,delete_disease

urlpatterns =[
    path('', home, name='home'),
    path('my_record/', my_record, name='my_record'),
    path('details/create', create_details, name='create_details'),
    path('details/<int:id>/update', update_details, name='update_details'),
    path('diseases/create', create_disease, name='create_disease'),
    path('diseases/<int:id>/update', update_disease, name='update_disease'),
    path('diseases/<int:id>/delete', delete_disease, name='delete_disease'),
]
