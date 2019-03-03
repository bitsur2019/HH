from django.db import models

# Create your models here.
class Usuario(models.Model):
    CI = models.CharField(max_length=8)
    Nombres = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    Teléfono = models.CharField(max_length=8)
    Celular = models.CharField(max_length=9)
    email = models.EmailField()
    Padrón = models.CharField(max_length=50)
    Torre = models.CharField(max_length=6)
    Apartamento = models.CharField(max_length=4, primary_key=True)
    Referencia = models.CharField(max_length=10)
    Estaciona_vehículo = models.CharField(max_length=2)
    Matrícula = models.CharField(max_length=20)