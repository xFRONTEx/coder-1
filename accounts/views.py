from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordChangeView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Perfil
from .forms import PerfilForm
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic.edit import UpdateView


class RegistroView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/registro.html'
    success_url = reverse_lazy('accounts:login')

class MyLoginView(LoginView):
    template_name = 'accounts/login.html'
    def get_success_url(self):
        # En esta parte incluyo la URL a la que me quiero redirijir después de iniciar sesión
        return reverse_lazy('core:home')
    
    
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
    login_url = '/accounts/login/'  # Redirige a esta URL si no está logueado

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Intentamos obtener el perfil, si no existe, lo creamos
        perfil, created = Perfil.objects.get_or_create(user=self.request.user)
        context['perfil'] = perfil
        context['user'] = self.request.user
        return context
    
@login_required
def profile_edit(request):
    user = request.user
    perfil, created = Perfil.objects.get_or_create(user=user)

    if request.method == 'POST':
        # Pasamos la instancia del usuario y del perfil para editar los existentes
        user_form = UserForm(request.POST, instance=user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil)
        
        # Validamos AMBOS formularios
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save() # Guarda nombre, apellido y email .
            perfil_form.save() # Guarda bio, avatar, etc. en el modelo Perfil.
            return redirect('accounts:profile')
    else:
        # Pre-llenamos con los datos actuales
        user_form = UserForm(instance=user)
        perfil_form = PerfilForm(instance=perfil)

    return render(request, 'accounts/profile_edit.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })

class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('accounts:profile') # Redirige al perfil al terminar
