from django.contrib import admin
from django.urls import path

from lms_app.views import dashboard

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
]




