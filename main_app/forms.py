from django.forms import ModelForm
from .models import Task, Project, Profile


# TASK ===============
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [ 'taskName', 'project' ]



# PROJECT ===============
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [ 'projectName' ]



# PROFILE ===============
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [ 'name' ]