from django.forms import ModelForm
from .models import Task, Project, Profile

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [ 'taskName', 'project' ]

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [ 'projectName' ]

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [ 'name' ]