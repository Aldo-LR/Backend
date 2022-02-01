from django.db import models

# Create your models here.

class Pregunta(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)

class Opcion(models.Model):
    nombre = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.RESTRICT)