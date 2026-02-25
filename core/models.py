from django.db import models

from django.db import models

class Feedback(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Tu Nombre")
    calificacion = models.IntegerField(choices=[(i, f"{i} Estrellas") for i in range(1, 6)])
    mensaje = models.TextField(verbose_name="¿Qué te parecieron los duendes?")
    opinion = models.TextField(verbose_name="¿Qué te pareció la experiencia en la aplicación?")
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.calificacion}★"
