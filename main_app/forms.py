from django.forms import ModelForm
from django import forms
from .models import Task, Project, Profile, Note, Time
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
        fields = ['name','email','image']



# NOTES ===============
class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = [ 'note' ]



# USERCREATION ===============
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=25)
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=150)

    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'password1', 'password2')


# TIME FORM ===============
class TimeForm(ModelForm):
    class Meta:
        model = Time
        fields = "__all__"

