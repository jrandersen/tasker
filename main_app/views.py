from django.shortcuts import render
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
  tasks = Task.objects.all()
  task_form = TaskForm()
  context = { 'tasks': tasks, 'task_form': task_form }
  return render(request, 'tasks/index.html', context )

def task_show(request, task_id):
  task = Task.objects.get(id=task_id)
  context = { 'task': task }
  return render( request, 'tasks/show.html', context )