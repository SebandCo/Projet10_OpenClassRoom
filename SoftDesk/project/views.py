from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers

class ProjectView(ModelViewSet):
    serializer_class = serializers.ProjectSerializer

    def get_queryset(self):
        return models.Project.objects.all()

# Create your views here.
