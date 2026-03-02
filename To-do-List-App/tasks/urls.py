from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_task, name='add_task'),
    path('complete/<int:pk>/', views.task_complete, name='task_complete'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('clear-completed/', views.clear_completed, name='clear_completed'),
]
