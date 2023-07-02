from rest_framework.permissions import BasePermission


class IsOwnerLocation(BasePermission):
    message = 'ليس لديك صلاحية لهذه'
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False