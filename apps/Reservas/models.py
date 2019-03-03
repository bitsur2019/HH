from django.db import models

# Create your models here.
class Reserva(models.Model):
    Parrillero = models.DateField()
    Comunal = models.DateField()
    
    