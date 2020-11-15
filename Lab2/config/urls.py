"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# dodanie ścieżki include
from django.urls import path, include
# aktualizacja by móc wyświetlać stronę główną; import wyświetlania szablonu
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    # muszą być powyżej, aby django szukał accounts jako pierwsze
    path('accounts/', include('accounts.urls')),
    # zawiera login, logout, zmiana hasła + done, resetowanie hasła + done, potwierdzenie
    path('accounts/', include('django.contrib.auth.urls')),
    # wyświetlanie strony głównej
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
