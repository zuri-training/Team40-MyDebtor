from rest_framework import permissions


class IsSchool (permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.groups.filter(name="School").exists()

        )
