import json

from django.http import JsonResponse, HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from .forms import RegistrationForm

from .models import Bug, Feedback, Project, Requirements, TaskPlanner, User

from .serializers import BugSerializer, FeedbackSerializer, ProjectSerializer, RequirementSerializer, TaskSerializer

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token



def apiOverview(request):
    return JsonResponse("API BASE POINT", safe=False)


@csrf_exempt
def loginUser(request):
    if request.method == 'POST':
        unicode = request.body.decode('utf-8')
        body = json.loads(unicode)
        username = body['username']
        password = body['password']
        user = authenticate(request, username=username, password=password)
        print(request)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            credentials = {
                "token" : str(token),
                "id" : user.id,
                "success" : True,
                "username" : username,
                "account_type" : user.type
            }
            response = JsonResponse(credentials)
            return response
        else:
            response = {
                'success': False,
                'message': 'Invalid username or password'
            }
            return JsonResponse(response)
    else:
        return JsonResponse({"error" : "Post request accepted only"})    


def signUp(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password =form.cleaned_data['password1']
            type = form.cleaned_data['type']
            user = authenticate(username=username, password=password)
            user.type = type
            user.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return HttpResponse("success")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})


@api_view(['GET'])
def logoutUser(request):
    user = request.user
    user.auth_token.delete()
    logout(request)
    return JsonResponse({"status" : "logged out"})
    

@api_view(['GET'])
def is_authenticated(request):
    return Response({"login_status" : True})
 

class ProjectRequirements(viewsets.ModelViewSet):
    queryset = Requirements.objects.all()
    serializer_class = RequirementSerializer


@api_view(['GET'])
def getRequirementsForProject(request, pk):
    requirements = Requirements.objects.all().filter(project=pk)
    serializer = RequirementSerializer(requirements, many=True)
    return Response(serializer.data)


class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

@api_view(['GET', 'POST'])
def getProjectForUser(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    projects = Project.objects.filter(user__in=[user])
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addUserToProject(request):
    try:
        body = json.loads(request.body)
        name = body['username']
        project_id = body['project_id']
        user = User.objects.get(username=name)
    except User.DoesNotExist:
        return Response({"found": False})
    project = Project.objects.get(id=project_id)
    project.user.add(user)
    return Response({
        "id": project_id,
        "members": list(project.user.all().values_list('username', flat=True)),
        "found": True 
    })
    

@api_view(['GET'])
def getUsersForProject(request, project_id):
    project = Project.objects.get(id=project_id)
    return Response({
        "id": project_id,
        "members": list(project.user.all().values_list('username', flat=True)),
    })


@api_view(['POST'])
def deleteUsersForProject(request):
    try:
        body = json.loads(request.body)
        name = body['member']
        project_id = body['project_id']
        user = User.objects.get(username=name)
        project = Project.objects.get(id = project_id)
        project.user.remove(user)
        return Response({"removed" : True})
    except:
        return Response({"removed" : False})


class ProjectBugs(viewsets.ModelViewSet):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer


@api_view(['GET'])
def getBugsForProject(request, pk):
    bug = Bug.objects.all().filter(project=pk)
    serializer = BugSerializer(bug, many=True)
    return Response(serializer.data)


class TaskView(viewsets.ModelViewSet):
    queryset = TaskPlanner.objects.all()
    serializer_class = TaskSerializer


class FeedbackView(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def create(self, request, *args, **kwargs):
        if not request.user:
            return Response({'detail': 'Authentication credentials were not provided.'})
        
        if request.user.type in ['E', 'A']:
            return super().create(request, *args, **kwargs)
        else:
            return Response({'detail': 'You do not have permission to perform this action.'})

    def update(self, request, *args, **kwargs):
        if not request.user:
            return Response({'detail': 'Authentication credentials were not provided.'})
        
        if request.user.type in ['E', 'A']:
            return super().update(request, *args, **kwargs)
        else:
            return Response({'detail': 'You do not have permission to perform this action.'})

    def retrieve(self, request, *args, **kwargs):
        if not request.user:
            return Response({'detail': 'Authentication credentials were not provided.'})
        
        if request.user.type in ['S', 'E', 'A']:
            return super().retrieve(request, *args, **kwargs)
        else:
            return Response({'detail': 'You do not have permission to perform this action.'})

    def list(self, request, *args, **kwargs):
        if not request.user:
            return Response({'detail': 'Authentication credentials were not provided.'})
        
        if request.user.type in ['S', 'E', 'A']:
            return super().list(request, *args, **kwargs)
        else:
            return Response({'detail': 'You do not have permission to perform this action.'})

    def destroy(self, request, *args, **kwargs):
        if not request.user:
            return Response({'detail': 'Authentication credentials were not provided.'})
        
        if request.user.type in ['E', 'A']:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response({'detail': 'You do not have permission to perform this action.'})    



