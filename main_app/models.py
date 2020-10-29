from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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

    def totaTime():
        # adds up all time per project 
        return null
    
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
        return self.taskName
    
    class Meta:
        ordering = ['-createdDate']
