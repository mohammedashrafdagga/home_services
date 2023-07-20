from rest_framework import permissions


# Order Permission to define Order for User
class OrderIsOwnerPermissions(permissions.BasePermission):
    # Owner for Show Ordering
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
    
    
class IsCompleteReviewPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.order.user == request.user and obj.order.order_status == 'مكتمل'



# permission for tracking app
class IsOwnerTracking(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user