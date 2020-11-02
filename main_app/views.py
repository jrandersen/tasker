from django.shortcuts import render, redirect
from .models import Profile, Project, Task, Note, Time
from .forms import TaskForm, ProjectForm, ProfileForm, SignUpForm, NoteForm, TimeForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from taggit.models import Tag
import datetime
from datetime import date, timedelta


# ADMIN ====================================
# --- LANDING PAGE ROUTE ---
def home(request):
  return render(request, 'home.html')

# --- ABOUT TASKER & AUTHOR ---
def about(request):
    return render( request, 'about.html' )

# --- SIGNUP NEW USER & CREATE NEW PROFILE WITH RECIEVER IN MODEL
def signup(request):
  error_message = ''
  form = SignUpForm(request.POST)
  if form.is_valid():
    user = form.save()
    user.refresh_from_db()
    user.profile.email = form.cleaned_data.get('email')
    user.profile.name = form.cleaned_data.get('name')
    user.save()
    # username = form.cleaned_data('user.username')
    # password = form.cleaned_data('password1')
    # user = authenticate(username=username, password=password)
    # login(request, user)
    return redirect('login')
  else:
    # error_message = 'Invalid sign up - try again'
    form = SignUpForm()
  context = {'form': form, 'error_message': error_message }
  return render( request, 'registration/signup.html', context )


# TASKS ====================================
# --- SHOW ALL TASKS & NEW TASK ROUTE ---
def tasks(request):
  if request.method == 'POST':
    taskName = request.POST.get('taskName')
    project = Project.objects.get(id=request.POST.get('project'))
    creator = Profile.objects.get(id=request.user.id)
    new_task = Task(taskName=taskName, creator=creator, project=project)
    new_task.taskComplete = False
    new_task.save()
    return redirect('tasks')
  tasks = Task.objects.filter(creator=request.user.profile)
  projects = Project.objects.filter(creator=request.user.profile)
  creator = Profile.objects.get(id=request.user.id)
  priorTasks = []
  for task in tasks:
    if task.createdDate < date.today() - timedelta(days=1):
      priorTasks.append(task)
  task_form = TaskForm()
  context = { 'tasks': tasks, 'task_form': task_form, 'projects': projects, 'priorTasks': priorTasks }
  return render(request, 'tasks/index.html', context )

# --- SHOW TASK ROUTE ---
def task_show(request, task_id):
  task = Task.objects.get(id=task_id)
  notes = task.note_set.all()
  times = Time.objects.filter(task=task_id)
  durations = []
  for time in times:
    durations.append(time.getDuration())
  totalTime = sum(durations, datetime.timedelta())
  context = {'task': task, 'notes': notes, 'times': times, 'totalTime': totalTime}
  return render(request, 'tasks/show.html', context)

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

# --- COMPLETE TASK ROUTE ---
def task_complete(request, task_id):
  task = Task.objects.get(id=task_id)
  notes = task.note_set.all()
  times = Time.objects.filter(task=task_id)
  durations = []
  for time in times:
    durations.append(time.getDuration())
  totalTime = sum(durations, datetime.timedelta())
  if len(times) == 0:
    return render(request, 'modal_complete_error.html')
  else:
    task.taskComplete = True
    task.taskCompletedDate = datetime.date.today()
    task.save()
  context = {'task': task, 'notes': notes, 'times': times, 'totalTime': totalTime}
  return render(request, 'tasks/show.html', context)

# --- UN-COMPLETE A TASK ROUTE ---
def task_uncomplete(request, task_id):
  task = Task.objects.get(id=task_id)
  notes = task.note_set.all()
  times = Time.objects.filter(task=task_id)
  durations = []
  for time in times:
    durations.append(time.getDuration())
  totalTime = sum(durations, datetime.timedelta())
  if task.taskComplete == True:
    task.taskComplete = False
    task.taskCompletedDate = None
    task.save()
  context = {'task': task, 'notes': notes, 'times': times, 'totalTime': totalTime}
  return render(request, 'tasks/show.html', context)

# --- DELETE TASK ROUTE ---
def task_delete(request, task_id):
  task = Task.objects.get(id=task_id)
  if task.creator.id == request.user.id:
    task.delete()
  return redirect('tasks')



# NOTES ====================================
# --- ADD NOTES ROUTE TO TASK ---
def note_add(request, task_id):
  if request.method == 'POST':
    note = request.POST.get('note')
    task = Task.objects.get(id=task_id)
    creator = Profile.objects.get(id=request.user.id)
    new_note = Note(note=note, task=task, creator=creator)
    new_note.save()
    return redirect('task_show', task_id=task_id)
  # this is in the Task_show page
  return render ('Nothing here yet')

def note_edit(request, note_id):
  note = Note.objects.get(id=note_id)
  task_id = note.task.id
  if request.method == 'POST':
    if request.user.id == note.creator.user.id:
      note_form = NoteForm(request.POST, instance=note)
      if note_form.is_valid():
        note_form.save()
        return redirect('task_show', task_id=task_id)
    else:
      return redirect('task_show', task_id=task_id)
  else:
    note_form = NoteForm(instance=note)
  context = {'note' : note, 'note_form': note_form }
  return render (request, 'notes/edit.html', context)

def note_delete(request, note_id):
  note = Note.objects.get(id=note_id)
  task_id = note.task.id
  note.delete()
  return redirect('task_show', task_id=task_id)    




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
    projectName = request.POST.get('project')
    creator = Profile.objects.get(id=request.user.id)
    new_project = Project(projectName=projectName, creator=creator)
    new_project.save()
  projects = Project.objects.filter(creator=request.user.profile)
  project_form = ProjectForm()  
  context = { 'projects': projects, 'project_form': project_form }
  return render(request, 'projects/index.html', context )

# --- PROJECT SHOW ROUTE ---
def project_show(request, project_id):
  project = Project.objects.get(id=project_id)
  tasks = Task.objects.filter(project=project_id)
  context = { 'project': project, 'tasks': tasks }
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
  project = Project.objects.get(id=project_id)
  if project.creator.id == request.user.id:
    project.delete()
  return redirect('projects')


# TIME ====================================
# --- ADD TIME TO TASK ---
def time_add(request):
  if request.method == 'POST':
    time_form = TimeForm(request.POST)
    print(time_form)
    if time_form.is_valid():
      time_form.save()
      # time_form.save_m2m()# <--- Django-Taggit docs say this if you save(commit=False)
    return redirect('tasks')
  tasks = Task.objects.filter(creator=request.user.profile)
  context = { 'tasks':tasks }
  return render (request, 'time/new.html', context)

# --- TIME EDIT ---
def time_edit(request, time_id):
  time = Time.objects.get(id=time_id)
  task_id = time.task.id
  if request.method == 'POST':
    if request.user.id == time.task.creator.user.id:
      time_form = TimeForm(request.POST, instance=time)
      if time_form.is_valid():
        time_form.save()
        return redirect('task_show', task_id=task_id)
    else:
      return redirect('task_show', task_id=task_id)
  else:
    time_form = TimeForm(instance=time)
  context = {'time' : time, 'time_form': time_form }
  return render (request, 'time/edit.html', context)

# --- TIME DELETE ---
def time_delete(request, time_id):
   time = Time.objects.get(id=time_id)
   if time.task.creator.id == request.user.id:
    time.delete()
    task_id = time.task.id
    return redirect('task_show', task_id=task_id)




 
