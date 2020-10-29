from django.shortcuts import render, redirect
from .models import Profile, Project, Task
from .forms import TaskForm, ProjectForm, ProfileForm
from django.http import HttpResponse


# ADMIN ====================================
# --- LANDING PAGE ROUTE ---
def home(request):
  return render(request, 'home.html')

# --- ABOUT TASKER & AUTHOR ---
def about(request):
    return render( request, 'about.html' )



# TASKS ====================================
# --- SHOW ALL TASKS & NEW TASK ROUTE ---
def tasks(request):
  if request.method == 'POST':
    task_form = TaskForm(request.POST)
    if task_form.is_valid():
      new_task = task_form.save(commit=False)
      new_task.taskComplete = False # will fail w/o declaring it false
      new_task.creator = request.user.profile
      new_task.save()
      return redirect('tasks')
  tasks = Task.objects.all()
  task_form = TaskForm()
  projects = Project.objects.all()
  context = { 'tasks': tasks, 'task_form': task_form, 'projects': projects }
  return render(request, 'tasks/index.html', context )

# --- SHOW TASK ROUTE ---
def task_show(request, task_id):
  task = Task.objects.get(id=task_id)
  context = { 'task': task }
  return render( request, 'tasks/show.html', context )

# --- EDIT TASK ROUTE ---
def task_edit(request, task_id):
  task = Task.objects.get(id=task_id)
  if request.method == 'POST':
    if request.user.id == task.creator.user.id:
      task_form = TaskForm(request.POST, instance=task)
      if task_form.is_valid():
        task_form.save()
        return redirect('task_show', task_id=task_id)
    else:
      return redirect('task_show', task_id=task_id)
  else:
    task_form = TaskForm(instance=task)
  context = { 'task': task, 'task_form': task_form }
  return render(request, 'tasks/edit.html', context)

# --- DELETE TASK ROUTE ---
def task_delete(request, task_id):
  Task.objects.get(id=task_id).delete()
  return redirect('tasks')



# NOTES ====================================
# --- ADD NOTES ROUTE TO TASK ---
def note_new(request):
  # do some stuff
  return ('Nothing here yet')

def note_edit(request):
  # do some stuff
  return ('Nothing here yet')

def note_delete(request):
  # do some stuff
  return ('Nothing here yet')    




# PROFILE ====================================
# --- PROFILE SHOW ROUTE ---
def profile_show(request, profile_id):
  profile = Profile.objects.get(id=profile_id)
  context = { 'profile': profile, 'projects': projects }
  return render(request, 'profile/show.html', context)

# --- PROFILE EDIT ROUTE ---
def profile_edit(request, profile_id):
  profile = Profile.objects.get(id=profile_id)
  if request.method == 'POST':
    if request.user.id == profile.user.id: 
      profile_form = ProfileForm(request.POST, instance=profile)
      if profile_form.is_valid():
        profile_form.save()
        return redirect('profile_show', profile_id=profile_id)
    else:
      return redirect('profile_show', profile_id=profile_id)
  else:
    profile_form = ProfileForm(instance=profile)
  context = { 'profile': profile, 'profile_form': profile_form}
  return render(request, 'profile/edit.html', context)



# PROJECTS ====================================
# --- SHOW ALL PROJECTS & NEW PROJECT ROUTE ---
def projects(request):
  if request.method == 'POST':
    project_form = ProjectForm(request.POST)
    if project_form.is_valid():
      new_project = project_form.save(commit=False)
      new_project.creator = request.user.profile
      new_project.save()
  projects = Project.objects.all()
  project_form = ProjectForm()  
  context = { 'projects': projects, 'project_form': project_form }
  return render(request, 'projects/index.html', context )

# --- PROJECT SHOW ROUTE ---
def project_show(request, project_id):
  project = Project.objects.get(id=project_id)
  context = { 'project': project }
  return render( request, 'projects/show.html', context )


# --- PROJECT SHOW ROUTE ---
def project_edit(request, project_id):
  project = Project.objects.get(id=project_id)
  if request.method == 'POST':
    if request.user.id == project.creator.user.id: 
      project_form = ProjectForm(request.POST, instance=project)
      if project_form.is_valid():
        project_form.save()
        return redirect('project_show', project_id=project_id)
    else:
      return redirect('project_show', project_id=project_id)
  else:
    project_form = ProjectForm(instance=project)
  context = { 'project': project, 'project_form': project_form}
  return render(request, 'projects/edit.html', context)

# --- PROJECT DELETE ROUTE ---
def project_delete(request, project_id):
  Project.objects.get(id=project_id).delete()
  return redirect('projects')