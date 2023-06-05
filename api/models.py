from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('S', 'Student'),
        ('E', 'Educator'),
        ('A', 'Admin'),
    ]
    type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, null=True)

class Project(models.Model):
    project_name = models.CharField(max_length=50, null=True)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.project_name

class Requirements(models.Model):
    requirement_description = models.CharField(max_length=200)
    priority_rating = models.IntegerField()
    completion_status = models.BooleanField()
    assigned_to = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.requirement_description

class Bug(models.Model):
    bug_description = models.CharField(max_length=200)
    bug_priority = models.IntegerField()
    resolution_status = models.BooleanField()
    resolver = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.bug_description

class TaskPlanner(models.Model):
    task_name = models.CharField(max_length=200)
    is_completed = models.BooleanField(null=True)
    requirement = models.ForeignKey(Requirements, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.task_name

class Feedback(models.Model):
    date_reviewed = models.DateTimeField()
    text = models.CharField(max_length=10000)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text