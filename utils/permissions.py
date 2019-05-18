from rest_framework import permissions

from users.models import AdminType


class IsAdminUser(permissions.BasePermission):
    """
    Check permission by admin type.
    """

    def has_permission(self, request, view):
        # Only admin user is available
        return bool(
            request.user.is_authenticated and request.user.admin_type in [AdminType.ADMIN, AdminType.SUPER_ADMIN])
