from django.forms import ModelForm
from .models import Task, Project

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['taskName']

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['projectName']