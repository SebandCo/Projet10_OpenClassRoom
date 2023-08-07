from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'can_be_contacted', 'can_data_be_shared')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("nom", "description", "type")


class IssueAdmin(admin.ModelAdmin):
    list_display = ("nom", "statut", "priorite", "attribution", "balise", "progression")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("description",)


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Issue, IssueAdmin)
admin.site.register(models.IssueComment, CommentAdmin)
