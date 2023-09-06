from django.urls import path
from pharmacies.views import create_pharmacy, update_pharmacy, delete_pharmacy

urlpatterns = [
    path('create/', create_pharmacy, name='create_pharmacy'),
    path('<int:id>/delete/', delete_pharmacy, name='delete_pharmacy'),
    path('<int:id>/update/', update_pharmacy, name='update_pharmacy'),
]
