from django.test import TestCase
from .models import User, Project, Requirements, Bug, TaskPlanner, Feedback
from django.utils import timezone


class UserTestCase(TestCase):
    def setUp(self):
        self.Jake = User.objects.create_user(username='Jake', password='%1R8AB5f4w3', type='S')
        self.Smith = User.objects.create_user(username='Smith', password='w549yXlrO9$L', type='E')

    def testUserType(self):
        self.assertEqual(self.Jake.type, 'S')
        self.assertEqual(self.Smith.type, 'E')

class ProjectTestCase(TestCase):
    def setUp(self):
        self.Jake = User.objects.create_user(username='Jake', password='%1R8AB5f4w3')
        self.asana = Project.objects.create(project_name='asana')
        self.asana.user.add(self.Jake)

    def testProjectUsers(self):
        self.assertEqual(self.asana.user.count(), 1)
        self.assertEqual(self.asana.user.first(), self.Jake)

class RequirementsTestCase(TestCase):
    def setUp(self):
        self.Jake = User.objects.create_user(username='Jake', password='%1R8AB5f4w3')
        self.asana = Project.objects.create(project_name='asana')
        self.asana.user.add(self.Jake)
        self.requirement = Requirements.objects.create(requirement_description='Display project requirements.', priority_rating=5, completion_status=False, assigned_to=self.Jake.username, project=self.asana)

    def testRequirementFields(self):
        self.assertEqual(self.requirement.requirement_description, 'Display project requirements.')
        self.assertEqual(self.requirement.priority_rating, 5)
        self.assertFalse(self.requirement.completion_status)
        self.assertEqual(self.requirement.assigned_to, self.Jake.username)

class BugTestCase(TestCase):
    def setUp(self):
        self.Jake = User.objects.create_user(username='Jake', password='%1R8AB5f4w3')
        self.asana = Project.objects.create(project_name='asana')
        self.asana.user.add(self.Jake)
        self.bug = Bug.objects.create(bug_description='Display button deletes project.', bug_priority=3, resolution_status=False, resolver=self.Jake.username, project=self.asana)

    def testBugFields(self):
        self.assertEqual(self.bug.bug_description, 'Display button deletes project.')
        self.assertEqual(self.bug.bug_priority, 3)
        self.assertFalse(self.bug.resolution_status)
        self.assertEqual(self.bug.resolver, self.Jake.username)


class TaskPlannerTestCase(TestCase):
    def setUp(self):
        self.Jake = User.objects.create_user(username='Jake', password='%1R8AB5f4w3')
        self.asana = Project.objects.create(project_name='asana')
        self.asana.user.add(self.Jake)
        self.requirement = Requirements.objects.create(requirement_description='Create a new project', priority_rating=5, completion_status=False, assigned_to=self.Jake.username, project=self.asana)
        self.task = TaskPlanner.objects.create(task_name='Make the server', is_completed=False, requirement=self.requirement)

    def testTaskFields(self):
        self.assertEqual(self.task.task_name, 'Make the server')
        self.assertFalse(self.task.is_completed)
        self.assertEqual(self.task.requirement, self.requirement)


class FeedbackTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Jake', password='%1R8AB5f4w3')
        self.project = Project.objects.create(project_name='asana')
        self.project.user.add(self.user)
        self.feedback = Feedback.objects.create(
            date_reviewed=timezone.now(),
            text='This is a feedback',
            project=self.project
        )

    def testFeedBack(self):
        self.assertTrue(isinstance(self.feedback, Feedback))
        self.assertEqual(str(self.feedback), self.feedback.text)
        max_length = self.feedback._meta.get_field('text').max_length
        self.assertEquals(max_length, 10000)
        self.assertEqual(self.feedback.project, self.project)
        self.assertTrue(self.feedback.date_reviewed <= timezone.now())
        self.assertEqual(str(self.feedback), self.feedback.text)
        
    


