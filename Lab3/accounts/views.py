from django.shortcuts import render
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserRegistrationForm

# dla wszystkich klas urls nie są ładowane podczas importowania, dlatego uzywamy lazy żeby załadować je kiedy będą dostępne

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('changed_successfully')

def changed(request):
    return render(request, 'registration/changed_successfully.html', {})

# Rejestracja za pomocą e-mail

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Tworzenie użytkownika bez zapisu
            new_user = user_form.save(commit=False)
            # Wybierz hasło
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Zapisanie użytkownika
            new_user.save()
            return render(request,
                          'registration/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'registration/register.html',
                  {'user_form': user_form})