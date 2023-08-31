from django.urls import path
from records.views import my_record

urlpatterns =[
    path('my_record/', my_record, name='my_record'),
]
