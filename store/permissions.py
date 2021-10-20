from rest_framework.permissions import AllowAny, BasePermission

#Your permissions here
class IsAuthenticatedAndOwner(BasePermission):
    message = 'You must be the owner of this object.'
    edit_methods = ('GET','DELETE','PUT','PATCH',)
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'Merchant':
            return True
        return obj.user == request.user