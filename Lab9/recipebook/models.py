from django.db import models

# Utworzenie modelu wpisu z przepisem
class Recipe(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    description = models.CharField(max_length=450,blank=False, default='')
    published = models.BooleanField(default=False)
