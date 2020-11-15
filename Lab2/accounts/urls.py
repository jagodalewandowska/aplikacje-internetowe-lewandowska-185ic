from django.urls import path

from .views import SignUpView

# importowanie widoku rejestracji
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]