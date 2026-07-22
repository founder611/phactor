
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('phactor_homepage/', views.phactor_homepage, name='phactor_homepage'),
]
    