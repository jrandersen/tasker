from django.forms import ModelForm
from django import forms
from .models import Task, Project, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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



# USERCREATION ===============
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=25, help_text='Username')
    email = forms.EmailField(max_length=150, help_text='Email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')