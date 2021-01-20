from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from records import views

# Trasowanie adresów URL
# Dzięki niej generowana jest adres podstrony, dzięki 
# czemu można wykonywać operacje na Records
# records/ -- to wszystkie wydarzenia
# records/id -- to tylko jedno zdarzenie (do edycji)

router = routers.DefaultRouter()
router.register(r'records', views.RecordView, 'records')

urlpatterns = [
    path('admin/', admin.site.urls),         
    path('api/', include(router.urls))
]