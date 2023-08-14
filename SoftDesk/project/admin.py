from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id', 'can_be_contacted', 'can_data_be_shared')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("nom", 'id', "description", "type")


class IssueAdmin(admin.ModelAdmin):
    list_display = ("nom", 'id', "statut", "priorite", "attribution", "balise", "progression")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("description", 'id', 'author')


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Issue, IssueAdmin)
admin.site.register(models.IssueComment, CommentAdmin)
