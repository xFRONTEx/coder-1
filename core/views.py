from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import FeedbackForm


def home(request):
    if request.method == 'POST':
        # Si el usuario envió el formulario
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos en la base de datos
            return redirect('home')  # Recarga para limpiar el formulario
    else:
        # Si el usuario solo entra a ver la página
        form = FeedbackForm()
    
    return render(request, 'core/chimuelito.html', {'form': form})


