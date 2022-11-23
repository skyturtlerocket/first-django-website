from django.urls import path
from . import views

urlpatterns = [
    path('', views.numbersense, name='Number Sense'),
]