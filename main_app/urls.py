from django.urls import path
from . import views

urlpatterns = [
    # LANDING, SIGNUP & ABOUT ===============
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup', views.signup, name='signup'),
    
    # TASK ===============
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:task_id>/', views.task_show, name='task_show'),
    path('tasks/<int:task_id>/edit/', views.task_edit, name='task_edit'),
    path('tasks/<int:task_id>/delete/', views.task_delete, name='task_delete'),
    
    # TIME ===============
    path('time/add/', views.time_add, name='time_add'),
    path('time/<int:time_id>/edit/', views.time_edit, name='time_edit'),
    
    # PROFILE & PROJECT =============== 
    path('profile/<int:profile_id>/', views.profile_show, name='profile_show'),
    path('profile/<int:profile_id>/edit/', views.profile_edit, name='profile_edit'),
    # path('profile/<int:profile_id>/delete/', views.profile_delete, name='profile_delete'),

    # PROFILE & PROJECT ===============
    path('projects/', views.projects, name='projects'),
    path('projects/<int:project_id>/', views.project_show, name='project_show'),
    path('projects/<int:project_id>/edit/', views.project_edit, name='project_edit'),
    path('projects/<int:project_id>/delete/', views.project_delete, name='project_delete'),

    # NOTES ===============
    path('note/<int:task_id>/add/', views.note_add, name='note_add'),
    path('note/<int:note_id>/edit/', views.note_edit, name='note_edit'),
    path('note/<int:note_id>/delete/', views.note_delete, name='note_delete'),

]