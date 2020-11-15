from django.shortcuts import render
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views import generic

# dla wszystkich klas urls nie są ładowane podczas importowania, dlatego uzywamy lazy żeby załadować je kiedy będą dostępne

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('changed-successfully')

def changed(request):
    return render(request, 'registration/changed-successfully.html', {})