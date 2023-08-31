from django.urls import path
from records.views import my_record, home

urlpatterns =[
    path('', home, name='home'),
    path('my_record/', my_record, name='my_record'),
]
