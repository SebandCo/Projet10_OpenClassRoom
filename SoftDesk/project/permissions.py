from rest_framework.permissions import BasePermission
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from . import models


class IsAuthor(BasePermission):

    def has_permission(self, request, view):
        # donne le body de la requete
        #print((request.data))
        print((view.get_queryset))
        id = request.resolver_match.kwargs.get("project")
        print(id)

        if 'project' in view.kwargs:
            project_id = view.kwargs['id_project']
            print(project_id)
        elif 'pk' in view.kwargs:
            project_id = view.kwargs['pk']
            print(project_id)
        # Permet d'obtenir le numéro d'ID
        # print(request.resolver_match.kwargs["pk"])
        #print(request.resolver_match.kwargs.get["nom"])


    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.author_id


class IsUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.id


class IsContributor(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user in obj.contributeur.all()


class IsProjectContributor(BasePermission):

    """message = "You do not have permission to perform this action. Must have copyright permission. You \
    are a contributor and cannot modify or delete other contributors. You must have author permissions."
    def has_permission(self, request, view):
        print (view.kwargs)
        #project = get_object_or_404(models.Project, id=view.kwargs['project'])
        #if request.user.id == project.author.id:
         #   return True
        return False"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if obj.issue:
                return request.user in obj.issue.project.contributeur.all()
            else:
                return request.user in obj.project.contributeur.all()
