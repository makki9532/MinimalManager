from django.contrib import admin
from .models import Bug, Feedback, TaskPlanner, User, Project, Requirements
from django.contrib.auth import get_user_model


User = get_user_model()

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Requirements)
admin.site.register(Bug)
admin.site.register(TaskPlanner)
admin.site.register(Feedback)


