from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('Main/', views.index, name='main'),
    path('About/', views.about, name='about'),
    path('Contacts/', views.contacts, name='contacts'),
    path('tasks/', views.tasks, name='tasks'),
]
