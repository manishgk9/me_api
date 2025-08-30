# from rest_framework.permissions import BasePermission

# class IsOwnerOrReadOnly(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in ('GET', 'HEAD', 'OPTIONS'):
#             return True
#         return obj.profile.user == request.user
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Allow read-only for everyone, but only the owner can modify or delete.
    Works for Profile, Project, Work, etc.
    """
    def has_object_permission(self, request, view, obj):
        # Always allow safe (read-only) methods
        if request.method in permissions.SAFE_METHODS:
            return True

        if hasattr(obj, "user"):
            return obj.user == request.user

        if hasattr(obj, "profile"):
            return obj.profile.user == request.user
        return False
