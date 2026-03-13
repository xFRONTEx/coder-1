from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=250, unique=True)
    categoria = models.CharField(max_length=250, default='Sin categoria')
    estatura = models.PositiveIntegerField(default=0, help_text="Estatura en cm")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = RichTextField(null=True, blank=True)
    esta_pedido = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='duendes/', null=True, blank=True)
    stock = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre}, {self.categoria} ,{self.estatura}, {self.precio}, ({self.descripcion}) , {self.esta_pedido}, {self.stock}, {self.fecha_creacion}"
    
