from django.db import models

# Create your models here.
class Comunicado(models.Model):
    Apartamento = models.CharField(max_length=4)
    Nombre = models.CharField(max_length=50)
    Celular = models.CharField(max_length=9)
    Queja = models.CharField(max_length=200)