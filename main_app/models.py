from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.db.models import Q, F
from datetime import datetime, date

from taggit.managers import TaggableManager


# MODEL PROFILE ====================================
class Profile(models.Model):
    name = models.CharField(max_length=50, blank=True)
    dateJoined = models.DateField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=150)
    image = models.URLField(max_length=250, default="https://semantic-ui.com/images/avatar/large/steve.jpg")

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
    createdDate = models.DateField(auto_now_add=True)
    taskComplete = models.BooleanField(auto_created=False)
    taskCompletedDate = models.DateField(null=True, blank=True)
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.taskName

    class Meta:
        ordering = ['project', 'createdDate']



# MODEL NOTES ====================================
class Note(models.Model):
    note = models.TextField()
    noteCreatedDate = models.DateField(auto_now=True)
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.note)



# MODEL TIME ====================================
class Time(models.Model):
    date = models.DateField()
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
                check=Q(startTime__lte=F('endTime')),
                name='startTime_before_endTime'
            )
        ]

    def getDuration(self):
        duration = datetime.combine(date.min, self.endTime) - datetime.combine(date.min, self.startTime)
        return duration
    
    def getTags(self):
        tags = []
        for tag in self.tags.all():
            tags.append(str(tag))
        return ', '.join(tags)

    def __str__(self):
        return str(self.date)