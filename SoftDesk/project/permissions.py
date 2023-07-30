from rest_framework.permissions import BasePermission

class IsAuthor(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return  request.user.id == obj.author_id
    
class IsContributor(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user in obj.contributeur.all()