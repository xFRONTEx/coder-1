# producto/admin.py
from django.contrib import admin
from .models import Producto # Importa tu modelo

# Registra el modelo
admin.site.register(Producto)