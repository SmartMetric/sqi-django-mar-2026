from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('hobbies/', views.hobbies),
    path('goals/', views.goals),
]