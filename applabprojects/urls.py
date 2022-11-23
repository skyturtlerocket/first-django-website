from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game1/', views.game1, name='game1'),
    path('game2/', views.game2, name='game2'),
]
