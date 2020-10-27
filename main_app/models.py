from django.db import models

# Create your models here.
class Task(models.Model):
    taskName = models.CharField(max_length=50)
    createdDate = models.DateField(auto_now=True)
    taskComplete = models.BooleanField(auto_created=False)
    taskCompletedDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.taskName