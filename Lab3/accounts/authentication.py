from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend


class EmailAuthBackend(object):
    """
    Authenticate using an e-mail address.
    """
    # Funkcja przyjmuje parametry jak username oraz hasło
    # Próba pobrania użytkownika który sprawdzi hasło za pomocą funkcji check password
    # porównując te z bazy danych
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    # pobranie użytkownika po jego ID, django używa backendu aby otrzymać zautentyfikowanego
    # użytkownika przez cały czas trwania sesji
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None