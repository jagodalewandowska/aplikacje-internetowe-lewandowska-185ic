from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# dla wszystkich klas urls nie są ładowane podczas importowania, dlatego uzywamy lazy żeby załadować je kiedy będą dostępne

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
