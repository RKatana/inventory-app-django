from rest_framework import permissions

class IsMerchant(permissions.BasePermission):
    edit_methods = ('GET','DELETE','PUT','PATCH',)

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'Merchant':
            return True
        if request.method not in self.edit_methods:
            return False
