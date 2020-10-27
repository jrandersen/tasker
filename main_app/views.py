from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render( request, 'about.html' )

def tasks(request):
  if request.method == 'POST':
    task_form = TaskForm(request.POST)
    if task_form.is_valid():
      new_task = task_form.save(commit=False)
      new_task.taskComplete = False # will fail w/o declaring it false
      new_task.save()
      return redirect('tasks')
  tasks = Task.objects.all()
  task_form = TaskForm()
  context = { 'tasks': tasks, 'task_form': task_form }
  return render(request, 'tasks/index.html', context )

def task_show(request, task_id):
  task = Task.objects.get(id=task_id)
  context = { 'task': task }
  return render( request, 'tasks/show.html', context )
