from rest_framework import permissions


class IsAdminRole(permissions.BasePermission):
    """
    Check permission by admin type.
    """

    def has_permission(self, request, view):
        # Only admin user is available
        return bool(request.user.is_authenticated and request.user.is_admin_role())
