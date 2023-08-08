from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from . import models
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

    def save(self):
        user = models.User(self)
        user.save()
        return user


class UserSerializer(ModelSerializer):

    class Meta:
        model = models.User
        fields = ["id", "username", "first_name", "last_name", "email", "age", "can_be_contacted", "can_data_be_shared"]


class UserCreationSerializer(ModelSerializer):

    class Meta:
        model = models.User
        fields = ["id", "username", "password", "first_name", "last_name", "email", "age", "can_be_contacted", "can_data_be_shared"]


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
            data = super().to_representation(instance)
            can_be_contacted = instance.can_be_contacted

            if not can_be_contacted:
                data.pop("email")

            return data

# Gestion des Projets


class ProjectCreationSerializer(ModelSerializer):
    
    class Meta:
        model = models.Project
        fields = ["nom", "author", "contributeur", "description", "type" ]


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

# Gestion des Issues


class IssueListSerializer(serializers.HyperlinkedModelSerializer):

    author = UserListSerializer()

    class Meta:
        model = models.Issue
        fields = ["id", "author", "nom", "priorite", "progression", "project"]


class IssueDetailSerializer(serializers.HyperlinkedModelSerializer):
    author = UserDetailSerializer()

    class Meta:
        model = models.Issue
        fields = ["id", "nom", "statut", "priorite", "balise", "progression", "project", "author", "attribution"]


class IssueCreationSerializer(ModelSerializer):

    class Meta:
        model = models.Issue
        fields = ["nom", "statut", "priorite", "balise", "progression", "project", "author", "attribution"]

# Gestion des IssueComment


class IssueCommentListSerializer(serializers.HyperlinkedModelSerializer):

    author = UserListSerializer()

    class Meta:
        model = models.IssueComment
        fields = ["id", "author", "issue"]


class IssueCommentDetailSerializer(serializers.HyperlinkedModelSerializer):
    author = UserDetailSerializer()

    class Meta:
        model = models.IssueComment
        fields = ["author", "issue", "description"]


class IssueCommentCreationSerializer(ModelSerializer):

    class Meta:
        model = models.IssueComment
        fields = ["author", "issue", "description"]
