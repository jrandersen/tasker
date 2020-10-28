from django.urls import path
from . import views

urlpatterns = [
    # ==== LANDING & ABOUT ==== #
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # ==== TASK ==== #
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:task_id>/', views.task_show, name='task_show'),
    path('tasks/<int:task_id>/edit/', views.task_edit, name='task_edit'),
    path('tasks/<int:task_id>/delete/', views.task_delete, name='task_delete'),

    # ==== PROFILE ==== #
    path('profile/<int:profile_id>/', views.profile_show, name='profile_show'),
    path('profile/<int:profile_id>/edit/', views.profile_edit, name='profile_edit'),

]