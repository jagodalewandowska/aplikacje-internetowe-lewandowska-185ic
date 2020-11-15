from django.urls import path
from . import views
from .views import SignUpView, PasswordsChangeView

# importowanie widoku rejestracji
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('change-password/', PasswordsChangeView.as_view(), name='change_password'),
    path('changed-successfully/', views.changed, name='changed_successfully'),
]