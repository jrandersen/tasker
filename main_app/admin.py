from django.contrib import admin
from .models import Profile, Project, Task

# REGISTER MODELS HERE ===============
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Task)
