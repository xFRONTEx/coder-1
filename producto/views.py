from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Producto
from django.views.generic.edit import DeleteView

# La lista de productos 
class ProductoListView(ListView):
    model = Producto
    template_name = 'producto/producto_list.html'
    context_object_name = 'productos'

# En esete caso, con el get_queryset, serviria para una busqueda específica pero por el momento no funciona.
def get_queryset(self):
        queryset = super().get_queryset()
        # Capturamos lo que el usuario escribe en el input llamado "buscar"
        query = self.request.GET.get('buscar')
        if query:
            # Filtramos por nombr es 
            queryset = queryset.filter(nombre__icontains=query)
        return queryset

# El formulario de Agregar (Crear)
class ProductoCreateView(CreateView):
    model = Producto
    fields = ['nombre', 'estatura', 'precio', 'descripcion', 'esta_pedido']
    template_name = 'producto/producto_crear.html'
    success_url = reverse_lazy('producto:lista')

# El formulario de Editar (Actualizar)
class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['nombre', 'estatura', 'precio', 'descripcion', 'esta_pedido']
    template_name = 'producto/producto_editar.html'
    success_url = reverse_lazy('producto:lista')

# El formulario de Eliminar (Borrar)
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto/producto_confirm_delete.html'
    success_url = reverse_lazy('producto:lista') # Redirige a la lista tras borrar