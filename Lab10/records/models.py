from django.db import models
from datetime import date

class Record(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  notes = models.CharField(max_length=200)
  finished = models.BooleanField(default=False)
  date = models.DateField(default=date.today)

  def _str_(self):
    return self.title
