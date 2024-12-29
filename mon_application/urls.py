from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('add-person/', views.add_person, name='add_person'),
    
]