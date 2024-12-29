from django.shortcuts import render, redirect
from .models import Person

def accueil(request):
    return render(request, 'mon_application/accueil.html')


def add_person(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age = request.POST['age']
        
        # Créer et sauvegarder une nouvelle personne dans la base de données
        person = Person(first_name=first_name, last_name=last_name, age=age)
        person.save()
        
        # Rediriger vers une page de confirmation (ou la même page)
        return redirect('add_person')  # Redirige vers la même page ou une autre page
    
    return render(request, 'mon_application/accueil.html')