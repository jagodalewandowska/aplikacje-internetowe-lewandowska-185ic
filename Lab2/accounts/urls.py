from django.urls import path
from . import views
from .views import SignUpView, PasswordsChangeView
from django.contrib.auth import views as auth_views

# importowanie widoku rejestracji
urlpatterns = [
    # Rejestracja
    path('signup/', SignUpView.as_view(), name='signup'),

    # Zmiana hasła + kiedy pomyślnie zmieinone
    path('change-password/', PasswordsChangeView.as_view(template_name = "registration/change_password.html"), name='change_password'),
    path('changed-successfully/', views.changed, name='changed_successfully'),

    # Resetowanie hasła
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset_form'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]