from django.shortcuts import render, redirect
from .models import Profile, Project, Task
from .forms import TaskForm, ProjectForm

# Create your views here.
from django.http import HttpResponse

# --- LANDING PAGE ROUTE ---
def home(request):
  return render(request, 'home.html')

# --- ABOUT TASKER & AUTHOR ---
def about(request):
    return render( request, 'about.html' )

# --- SHOW ALL TASKS & NEW TASK ROUTE ---
def tasks(request):
  if request.method == 'POST':
    task_form = TaskForm(request.POST)
    if task_form.is_valid():
      new_task = task_form.save(commit=False)
      new_task.taskComplete = False # will fail w/o declaring it false
      new_task.creator = request.user.profile
      new_task.save()
      return redirect('tasks')
  tasks = Task.objects.all()
  task_form = TaskForm()
  context = { 'tasks': tasks, 'task_form': task_form }
  return render(request, 'tasks/index.html', context )

# --- SHOW TASK ROUTE ---
def task_show(request, task_id):
  task = Task.objects.get(id=task_id)
  context = { 'task': task }
  return render( request, 'tasks/show.html', context )

# --- DELETE TASK ROUTE ---
def task_delete(request, task_id):
  Task.objects.get(id=task_id).delete()
  return redirect('tasks')

# --- PROFILE SHOW & NEW PROJECT ROUTE ---
def profile_show(request, profile_id):
  profile = Profile.objects.get(id=profile_id)
  if request.method == 'POST':
    project_form = ProjectForm(request.POST)
    if project_form.is_valid():
      new_project = project_form.save(commit=False)
      new_project.creator = request.user.profile
      new_project.save()
      # return redirect('profile/show.html')
  projects = profile.project_set.all()
  context = { 'profile': profile, 'projects': projects }
  return render(request, 'profile/show.html', context)


# --- PROFILE EDIT ROUTE ---


