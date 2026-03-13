"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls", namespace="core")), ## Esto hace posible que el link de vuelta a chimuelito funcione, ya que ahora las URLs de la app core están incluidas en el proyecto principal y se pueden referenciar con el namespace core.
    path('accounts/', include('accounts.urls', namespace="accounts")),
    path("producto/", include("producto.urls", namespace="producto")), ## Esto es lo que le dice a Django que incluya las URLs de la app producto y que use el namespace producto para referenciar esas URLs.
]

# ESTO VINCULA TU MEDIA_URL CON TU MEDIA_ROOT
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
