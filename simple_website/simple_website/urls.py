from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('profile/', views.profile),
    path('services/', views.services),
    path('help/', views.help_page),
]