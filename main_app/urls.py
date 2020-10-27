from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:task_id>/', views.task_show, name='task_show'),
    path('tasks/<int:task_id>/delete/', views.task_delete, name='task_delete'),

]