from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsProjectUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user in obj.contributeur.all()
        else:
            return request.user.id == obj.author_id


class IsAuthor(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.id == obj.author_id


class IsUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.id
