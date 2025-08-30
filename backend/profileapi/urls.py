from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, ProjectViewSet, health, RegisterView, SkillViewSet ,WorkExperienceViewSet      
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register('profiles', ProfileViewSet, basename='profile')
router.register('projects', ProjectViewSet, basename='project')
router.register('skills', SkillViewSet, basename='skills')
router.register('work-experience', WorkExperienceViewSet, basename='workexperience')

urlpatterns = [
    path('', include(router.urls)),
    path('health/', health, name='health'),
    path('auth/token/', obtain_auth_token, name='token'),
    path('auth/register/', RegisterView.as_view(), name='register'),
]
