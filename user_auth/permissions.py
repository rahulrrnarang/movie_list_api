from rest_framework import permissions

class OwnerOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.collection_creator == request.user