from django.urls import path
from records.views import my_record, home, create_details, update_details
urlpatterns =[
    path('', home, name='home'),
    path('my_record/', my_record, name='my_record'),
    path('details/create/', create_details, name='create_details'),
    path('details/<int:id>/update/', update_details, name='update_details'),
]
