from django.urls import path
from .views import MyLoginView
from .views import ProfileView
from .views import RegistroView
from django.contrib.auth.views import LogoutView

from . import views
from .views import MyPasswordChangeView

app_name = 'accounts'

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('logout/', LogoutView.as_view(next_page='accounts:login'), name='logout'),
    path('edit/', views.profile_edit, name='profile_edit'),
    path('password_change/', MyPasswordChangeView.as_view(), name='password_change'),
]