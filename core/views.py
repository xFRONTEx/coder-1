from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm
from django.contrib.auth.views import LoginView

# Aplicamos el decorador para proteger la home
@login_required(login_url='accounts:login')
def home(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = FeedbackForm()
    
    return render(request, 'core/base.html', {'form': form})

@login_required
def blog_duendes(request):
    return render(request, 'core/blog_duendes.html')

@login_required
def acercade_mi(request):
    return render(request, 'core/acercade-mi.html')

# Esta vista no lleva @login_required porque es el Login mismo
class MyLoginView(LoginView):
    template_name = 'accounts/login.html'