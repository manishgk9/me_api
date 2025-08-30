from rest_framework import viewsets, filters, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from django.http import JsonResponse
from .models import Profile, Project, Skill, WorkExperience
from .serializers import  ProfileSerializer, ProjectSerializer, SkillsSerializer, WorkSerializer, RegisterSerializer
from .custom_permissions import IsOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().prefetch_related('skills', 'projects', 'work')
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'full_name', 'email', 'education', 'bio',
        'projects__title', 'projects__description', 'skills__name'
    ]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().select_related('profile').prefetch_related('skills').order_by('-created_at')
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'skills__name']

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

    def get_queryset(self):
        qs = super().get_queryset()
        skill = self.request.query_params.get('skill')
        if skill:
            qs = qs.filter(skills__name__icontains=skill)
        return qs


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class WorkExperienceViewSet(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['company', 'role', 'description']

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


@api_view(['GET'])
def health(request):
    return Response({"status": "ok"})


def custom_404(request, exception):
    return JsonResponse({"error": "Bad Request. The requested resource was not found."}, status=404)

def custom_500(request):
    return JsonResponse({"error": "Internal Server Error. Please try again later."}, status=500)


class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "success": True,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            }
        }, status=status.HTTP_201_CREATED)
