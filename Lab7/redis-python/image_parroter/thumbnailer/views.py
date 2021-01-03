import os

from celery import current_app

from django import forms
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from .tasks import make_thumbnails

# formularz wysyłania obrazów
class FileUploadForm(forms.Form):
    image_file = forms.ImageField(required=True)

# widok strony głównej, posiada 
# formularz oraz pole ImageField
class HomeView(View):
    def get(self, request):
        form = FileUploadForm()
        return render(request, 'thumbnailer/home.html', { 'form': form })
    
    # tworzenie obiektu FileUploadForm
    def post(self, request):
        form = FileUploadForm(request.POST, request.FILES)
        context = {}

        # jeśli formularz poprawny, zapisywanie pliku do IMAGES_DIR
        if form.is_valid():
            file_path = os.path.join(settings.IMAGES_DIR, request.FILES['image_file'].name)

            # obsługa przesyłanego pliku
            with open(file_path, 'wb+') as fp:
                for chunk in request.FILES['image_file']:
                    fp.write(chunk)

            # uruchomienie tworzenia miniatury - thumbnail
            task = make_thumbnails.delay(file_path, thumbnails=[(128, 128)])

            # pobranie id zadania oraz statusu
            context['task_id'] = task.id
            context['task_status'] = task.status

            return render(request, 'thumbnailer/home.html', context)

        # jeśli formularz nie jest poprawny, zwraca z błędami do podstawowego
        context['form'] = form

        return render(request, 'thumbnailer/home.html', context)

# używane przez AJAX, by sprawdzić status make_thumbnails, import current_app
# następnie pobieranie asyncresult obiektu z id zawartego w żądaniu
class TaskView(View):
    def get(self, request, task_id):
        task = current_app.AsyncResult(task_id)
        response_data = {'task_status': task.status, 'task_id': task.id}

        # jeśli zadanie wykonane pomyślnie pobieranie wyników results 
        # a następnie wywołanie metody get przypisując do wyników jako
        # json do żądania http
        if task.status == 'SUCCESS':
            response_data['results'] = task.get()

        return JsonResponse(response_data)