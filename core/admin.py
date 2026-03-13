from django.contrib import admin
from .models import Feedback  # Importamos tu modelo

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    # Esto define qué columnas verás en la lista
    list_display = ('nombre', 'calificacion', 'mensaje')