from django import forms
from django.contrib.auth.models import User
from .models import Perfil

# 1. Formulario para los datos del usuario (Nombre, Apellido, Email)
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico'
        }

    def _init_(self, *args, **kwargs):
        super(UserForm, self)._init_(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs.update({'class': 'input-pergamino'})

# 2. Formulario para los datos del perfil (Avatar, Bio, Fecha)
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar', 'bio', 'fecha_nacimiento']
        labels = {
            'avatar': 'Elige tu foto de perfil.',
            'bio': 'Tu biografía/vendedor',
            'fecha_nacimiento': 'Fecha de nacimiento'
        }
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def _init_(self, *args, **kwargs):
        super(PerfilForm, self)._init_(*args, **kwargs)
        for field in self.visible_fields():
            # Aplic amos la clase  CSS a todos los campos..
            field.field.widget.attrs.update({'class': 'input-pergamino'})