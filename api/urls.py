from django.urls import path, include
from . import views
from .views import ProjectBugs, ProjectView, ProjectRequirements, TaskView, FeedbackView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('project', ProjectView)
router.register('requirements', ProjectRequirements)
router.register('bugs', ProjectBugs)
router.register('tasks', TaskView)
router.register('feedback', FeedbackView)


urlpatterns = [
    path('test', views.apiOverview ,name='api-overview'),
    path('login', views.loginUser ,name='login'),
    path('signup', views.signUp, name='signup'),
    path('logout/', views.logoutUser ,name='logout'),
    path('auth/', views.is_authenticated ,name='auth'),
    path('getRequirementsForProject/<str:pk>/', views.getRequirementsForProject ,name='getRequirementsForProject'),
    path('getProjectForUser/<str:user_id>/', views.getProjectForUser ,name='getProjectForUser'),
    path('addUserToProject/', views.addUserToProject ,name='addUserToProject'),
    path('getUsersForProject/<str:project_id>/', views.getUsersForProject ,name='getUsersForProject'),
    path('deleteUsersForProject/', views.deleteUsersForProject ,name='deleteUsersForProject'),
    path('getBugsForProject/<str:pk>/', views.getBugsForProject ,name='getBugsForProject'),
    path('', include(router.urls)),
]

