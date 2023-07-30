from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from . import models

class ProjectSerializer(ModelSerializer):

    class Meta:
        model = models.Project
        fields = ["id", "nom", "author", "description", "type", "contributeur", "created_time"]

class UserSerializer(ModelSerializer):   

    class Meta:
        model = models.User
        fields = ["username", "first_name", "last_name", "email", "age", "can_be_contacted", "can_data_be_shared"]

class IssueSerializer(ModelSerializer):

    class Meta:
        model = models.Issue
        fields = ["id", "nom", "statut", "priorite", "author", "attribution", "balise", "progression", "contributeur"]


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ("username", "password", "first_name", "last_name", "email", "age", "can_be_contacted", "can_data_be_shared")

    def save(self):
        user = models.User(self)
        user.save()
        return user