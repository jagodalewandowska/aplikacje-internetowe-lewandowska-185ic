from django.contrib import admin
from .models import Record

# Wyświetlanie listy dodanych elementów w modelu
class RecordsAdmin(admin.ModelAdmin):
  list_display = ('title', 'description', 'notes', 'finished', 'date')

# Rejestrowanie Records oraz RecordsAdmin
admin.site.register(Record, RecordsAdmin)