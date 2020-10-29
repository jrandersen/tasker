from django.contrib import admin
from .models import Profile, Project, Task, Note, Time

# REGISTER MODELS HERE ===============
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Note)
admin.site.register(Time)
