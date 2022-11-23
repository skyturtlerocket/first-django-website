from django.urls import path
from . import views

urlpatterns = [
    path('', views.aboutcreator2, name='About Creator 2'),
]