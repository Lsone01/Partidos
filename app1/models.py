from django.db import models

class PartidoPolitico(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)
    presidente = models.CharField(max_length=100)
    fundacion = models.DateField()

    def __str__(self):
        return self.nombre
