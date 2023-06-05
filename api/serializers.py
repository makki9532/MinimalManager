from rest_framework import serializers
from .models import Bug, Feedback, TaskPlanner, User, Project, Requirements

class LoginSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'password')

class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = "__all__"


class RequirementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Requirements
		fields = ('id','project', 'requirement_description','priority_rating','completion_status', 'assigned_to')
		

class BugSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bug
		fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = TaskPlanner
		fields = "__all__"

class FeedbackSerializer(serializers.ModelSerializer):
	class Meta:
		model = Feedback
		fields = "__all__"