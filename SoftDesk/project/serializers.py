from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from . import models
from collections import OrderedDict
""" Chaque models a deux Serializers
- ***ListSerializer : Vue d'ensemble des models
- ***DetailSerializer : Vue de détail d'un model

Pour les Serializers basé sur HyperlinkedModelSerializer un autre serializer a été rajouté
- ***CreationSerializer : Permet de créer un model en utilisant l'id du model lié"""

# Gestion des Utilisateurs


class RegistrationSerializer(ModelSerializer):

    class Meta:
        model = models.User
        fields = ["username", "password", "first_name", "last_name", "email", "age", "can_be_contacted", "can_data_be_shared"]

    def create(self, validate_data):
        print("test")
        user = models.User(self)
        user.set_password(validate_data.get("password"))
        user.save()
        return user


class UserSerializer(ModelSerializer):

    class Meta:
        model = models.User
        fields = ["id", "username", "password", "first_name", "last_name", "email", "age", "can_be_contacted", "can_data_be_shared"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["password"] = "password secret"
        return representation

class UserCreationSerializer(ModelSerializer):

    class Meta:
        model = models.User
        fields = ["username", "password", "first_name", "last_name", "email", "age", "can_be_contacted", "can_data_be_shared"]


class UserListSerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = ["username"]


class UserContactedSerializer(serializers.RelatedField):

    class Meta:
        model = models.User
        fields = ["id", "username", "first_name", "last_name", "email", "age"]


class UserDetailSerializer(ModelSerializer):

    class Meta:
        model = models.User
        fields = ["id", "username", "first_name", "last_name", "email", "age", "can_be_contacted", "can_data_be_shared"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        can_be_contacted = instance.can_be_contacted
        can_data_be_shared = instance.can_data_be_shared

        if can_be_contacted is False:
            representation["email"] = "Ne souhaite pas être contacté"

        if can_data_be_shared is False:
            representation["first_name"] = "Ne souhaite pas être partagé"
            representation["last_name"] = "Ne souhaite pas être partagé"
            representation["age"] = "Ne souhaite pas être partagé"

        return representation

# Gestion des Projets


class ProjectCreationSerializer(ModelSerializer):

    class Meta:
        model = models.Project
        fields = ["nom", "author", "contributeur", "description", "type"]


class ProjectListSerializer(ModelSerializer):

    author = UserListSerializer()

    def create(self, validated_data):
        return models.Project.objects.create(**validated_data)

    class Meta:
        model = models.Project
        fields = ["id", "nom", "author", "contributeur", "description", "type"]


class ProjectDetailSerializer(ModelSerializer):

    author = UserDetailSerializer()

    class Meta:
        model = models.Project
        fields = ["id", "nom", "author", "description", "type", "contributeur", "created_time"]
        read_only_fields = ["id", "author", "created_time"]

# Gestion des Issues


class IssueListSerializer(ModelSerializer):

    author = UserListSerializer()

    class Meta:
        model = models.Issue
        fields = ["id", "author", "nom", "priorite", "progression", "project"]


class IssueDetailSerializer(serializers.HyperlinkedModelSerializer):
    author = UserDetailSerializer()
    
    class Meta:
        
        model = models.Issue
        fields = ["id", "nom", "statut", "priorite", "balise", "progression", "project", "author", "attribution", "created_time"]
        read_only_fields = ["id", "project", "author", "created_time"]


class IssueCreationSerializer(ModelSerializer):

    class Meta:
        model = models.Issue
        fields = ["nom", "statut", "priorite", "balise", "progression", "project", "author", "attribution"]

# Gestion des IssueComment


class IssueCommentListSerializer(serializers.HyperlinkedModelSerializer):

    author = UserListSerializer()

    class Meta:
        model = models.IssueComment
        fields = ["id", "author", "issue", "project"]


class IssueCommentDetailSerializer(serializers.HyperlinkedModelSerializer):
    author = UserDetailSerializer()
    
    class Meta:
        model = models.IssueComment
        fields = ["id","author", "issue", "description", "created_time", "project"]
        read_only_fields = ["id", "author", "issue", "created_time"]
    

class IssueCommentCreationSerializer(ModelSerializer):

    class Meta:
        model = models.IssueComment
        fields = ["author", "issue", "description"]

    # Affecte automatiquement le project lié à l'issue lors de la création du Comment
    def create(self, validated_data):
        id_issue = validated_data["issue"].id
        issue = models.Issue.objects.get(id=id_issue)
        id_project = issue.project
        validated_data["project"] = id_project
        return models.IssueComment.objects.create(**validated_data)
