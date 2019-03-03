from django.db import models

# Create your models here.
class Contacto(models.Model):
    OTIS = models.CharField(max_length=10)
    Administración = models.CharField(max_length=10)
    Mantenimiento = models.CharField(max_length=10)