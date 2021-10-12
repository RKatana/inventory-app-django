from rest_framework import permissions

class IsOwnerorReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    # if request.method in permissions.permissions.SAFE_METHODS
