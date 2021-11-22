from django.urls import path, include
from . import views

urlpatterns = [
    path('animals/', views.animals, name='all_animals'),
    path('animal/<int:animal_id>/', views.animal, name='single_animal'),
    path('family/<int:family_id>/', views.family, name='family')
]