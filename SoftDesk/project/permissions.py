from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsAuthor(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.author_id


class IsUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.id


class IsContributor(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS and request.user in obj.contributeur.all():
            return request.user in obj.contributeur.all()


class IsProjectContributor(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS and request.user in obj.project.contributeur.all():
            return request.user in obj.project.contributeur.all()
