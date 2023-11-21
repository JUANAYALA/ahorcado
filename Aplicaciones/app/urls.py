from django.urls import path
from . import views

urlpatterns = [
    path('nuevo_juevo', views.nuevo_juego, name='nuevo_juego'),
    path('', views.inicio, name='inicio'),
    path('juego/<int:juego_letra>/', views.jugar, name='jugar'),
]