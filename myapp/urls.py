from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.users, name='users'),
    path('users/details/<slug:slug>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('minigame/', views.minigame, name='minigame')
]