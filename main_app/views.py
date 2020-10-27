from django.shortcuts import render

class Task:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, project):
    self.name = name
    self.project = project

basic_tasks = [
  Task('Do this', 'client-one'),
  Task('Do that', 'client-one'),
  Task('Do something', 'client-one'),
]


# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def tasks(request):
  context = { 'basic_tasks': basic_tasks }
  return render(request, 'tasks/index.html', context )