import os
from zipfile import ZipFile

from celery import shared_task
from PIL import Image

from django.conf import settings

@shared_task
def make_thumbnails(file_path, thumbnails=[]):
    # zmiana bieżącego katalogu
    os.chdir(settings.IMAGES_DIR)
    # rozdzielenie nazwy ścieżki na nagłówek i end
    path, file = os.path.split(file_path)
    # podział ścieżki na root oraz ext
    file_name, ext = os.path.splitext(file)
    # miejsce przechowywania root z rozszerzeniem
    # *.zip
    zip_file = f"{file_name}.zip"
    # zwracanie url końcowego
    results = {'archive_path': f"{settings.MEDIA_URL}images/{zip_file}"}
    try:
        # otwieranie obrazu
        img = Image.open(file_path)
        # wykorzystywanie zaimportowanego ZipFile 
        # i utworzenie nowego
        zipper = ZipFile(zip_file, 'w')
        # zapisanie nowego pliku o nazwie w nawiasie - file
        zipper.write(file)
        # usuwanie ścieżki pliku
        os.remove(file_path)
        for w, h in thumbnails:
            # kopiowanie obrazu i obliczanie wymiarów na miniaturę,
            # gdzie w to width oraz h to height
            img_copy = img.copy()
            img_copy.thumbnail((w, h))
            thumbnail_file = f'{file_name}_{w}x{h}.{ext}'
            # zapisanie kopii oryginalnego obrazu, zapisanie miniatury 
            # do archiwum oraz usuwanie ścieżki pliku z miniaturą
            img_copy.save(thumbnail_file)
            zipper.write(thumbnail_file)
            os.remove(thumbnail_file)
        # zamykanie
        img.close()
        zipper.close()

    # wyłapanie błędu przy niepowodzeniu 
    except IOError as e:
        print(e)

    # zwracanie url do pobrania pliku
    return results

@shared_task
def multiply(x, y):
    return x * y

@shared_task
def divide(x, y):
    return x / y