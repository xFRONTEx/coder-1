from django.urls import path
from . import views

app_name = 'producto'

urlpatterns = [
    # Cambia 'views.producto_list' por 'views.ProductoListView.as_view()'
    path('', views.ProductoListView.as_view(), name='lista'),
    
    # Ruta para crear
    path('nuevo/', views.ProductoCreateView.as_view(), name='crear'),
    
    # Ruta para editar
    path('editar/<int:pk>/', views.ProductoUpdateView.as_view(), name='editar'),

    # Ruta para eliminar
    path('eliminar/<int:pk>/', views.ProductoDeleteView.as_view(), name='eliminar'),
]