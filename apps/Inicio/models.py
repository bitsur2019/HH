from django.db import models

# Create your models here.
class Inicio(models.Model):
    Notificaciones = models.CharField(max_length=100)
    