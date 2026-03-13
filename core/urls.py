from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = "core"

urlpatterns = [
    path("", views.home, name='home'),
    path('blog/', views.blog_duendes, name='blog'),
    path('acercade/', views.acercade_mi, name='acercade'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    ]