from django.db import models
from django.utils import timezone

#  ta linijka definiuje nasz model; post - model, models.Model - informacja dla Django aby przechowywać obiekt w baze danych
class Post(models.Model):
    # foreignKey - odnosnik do innego modelu
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # tekst z ograniczona iloscia znakow
    title = models.CharField(max_length=200)
    # bez ograniczen tekst
    text = models.TextField()    
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # metoda publikujaca

    def __str__(self):
        return self.title