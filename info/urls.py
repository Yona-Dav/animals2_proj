from django.urls import path, include
from . import views

urlpatterns = [
    path('animals/', views.animals, name='all_animals'),
    path('animal/<int:animal_id>/', views.animal, name='single_animal'),
    path('family/<int:fami_id>/', views.family, name='family'),
    path('animals/<int:speed>/', views.speed, name='speed_animal')
]