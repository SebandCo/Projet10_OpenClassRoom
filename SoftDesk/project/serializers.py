from rest_framework.serializers import ModelSerializer

from . import models

class ProjectSerializer(ModelSerializer):

    class Meta:
        model = models.Project
        fields = ["id", "nom", "author", "description", "type", "contributeur", "created_time"]
