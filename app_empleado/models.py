# app_empleado/models.py

from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.nombre} - {self.puesto}'