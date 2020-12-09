from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from .views import HomePageView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('scraping/', views.getHtml, name="scraping"),
    path('scrapped/', views.getHtml, name="scrapped"),
    path('xpath/', views.xml, name="xpath"),
    path('labs/', views.labs, name="labs"),
]