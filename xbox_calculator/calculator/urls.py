from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate_conversion, name='calculate_conversion'),
]
