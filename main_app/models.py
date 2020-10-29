from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.db.models import Q, F

from taggit.managers import TaggableManager


# MODEL PROFILE ====================================
class Profile(models.Model):
    name = models.CharField(max_length=50, blank=True)
    dateJoined = models.DateField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=150)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



# MODEL PROJECT ====================================
class Project(models.Model):
    projectName = models.CharField(max_length=50)
    startDate = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.projectName
  
    class Meta:
        ordering = ['-startDate']



# MODEL TASK ====================================
class Task(models.Model):
    taskName = models.CharField(max_length=50)
    createdDate = models.DateField(auto_now=True)
    taskComplete = models.BooleanField(auto_created=False)
    taskCompletedDate = models.DateField(null=True, blank=True)
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.taskName + self.taskComplete + self.taskCompletedDate
    
    class Meta:
        ordering = ['-createdDate']



# MODEL NOTES ====================================
class Note(models.Model):
    note = models.TextField()
    noteCreatedDate = models.DateField(auto_now=True)
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.note + self.noteCreatedDate + self.creator + self.task



# MODEL TIME ====================================
class Time(models.Model):
    date = models.DateField(auto_now=True)
    startTime = models.TimeField()
    endTime = models.TimeField()
    tags = TaggableManager()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def clean(self):
        if self.startTime > self.endTime:
            raise ValidationError('Start time should be before end time')
        return super().clean()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(start_lte=F('endTime')),
                name='startTime_before_endTime'
            )
        ]

    def totaTime():
        # adds up all time per project 
        return 0

    def __str__(self):
        return self.date + self.startTime + self.endTime + self.tags + self.task
