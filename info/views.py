from django.shortcuts import render
from .models import Animal, Family
from django.db.models import Count

# Create your views here.

def animals(request):
    animals = Animal.objects.all().order_by('family__name','name')
    return render(request, 'animals.html', {'animals': animals})

def animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    return render(request, 'animal.html', {'animal': animal})

def family(request, fami_id):
    family = Family.objects.get(id=fami_id)
    calc = Animal.objects.filter(family_id=fami_id).annotate(num_ani = Count('family_id'))
    return render(request, 'family.html', {'family': family, 'num_animals': len(calc)})

def speed(request,speed):
    speeds = Animal.objects.filter(speed__gt=speed).order_by('speed')
    return render(request, 'speed.html', {'speeds': speeds})