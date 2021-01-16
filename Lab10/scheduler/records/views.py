from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RecordSerializer
from .models import Record

class RecordView(viewsets.ModelViewSet):
  serializer_class = RecordSerializer
  queryset = Record.objects.all()  