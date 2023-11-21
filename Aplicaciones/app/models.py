from django.db import models

# Create your models here.
class Words(models.Model):
    palabra = models.CharField(max_length=50)
    letras_incorrectas = models.CharField(max_length=50 , default="")
    letras_adivinadas = models.CharField(max_length=50,  default="")
    intentos_restantes = models.IntegerField(default=6)