from django.db import models

# Create your models here.
class Finanza(models.Model):
    Gastos_Comunes = models.CharField(max_length=10)
    Sueldos = models.CharField(max_length=10)
    Gastos_Generales = models.CharField(max_length=10)