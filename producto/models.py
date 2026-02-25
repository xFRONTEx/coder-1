from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=250, unique=True)
    estatura = models.PositiveIntegerField(default=0, help_text="Estatura en cm")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(null=True, blank=True)

    
    esta_pedido = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.nombre}, {self.estatura}, {self.precio}, ({self.descripcion}) , {self.esta_pedido}"
    
