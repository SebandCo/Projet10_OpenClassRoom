from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password

from .permissions import IsAuthor, IsContributor, IsProjectContributor, IsProjectUser

from . import models
from . import serializers

"""Chaque View peut se décliner en deux versions
- serializer_class : donne un aperçu de tout les models
- detail_serializer_class : donne un détail d'un model en particulier

La création d'un model lié à un autre model se fait via l'id du model à choisir
"""


class ProjectView(ModelViewSet):
    serializer_class = serializers.ProjectListSerializer
    detail_serializer_class = serializers.ProjectDetailSerializer
    permission_classes = [IsAuthenticated & IsProjectUser]

    def get_queryset(self):
        return models.Project.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        else:
            return super().get_serializer_class()

    def create(self, request, format=None):
        # Affecte automatiquement l'auteur et le contributeur si il n'existe pas
        if request.data:
            request.data._mutable = True
            request.data["author"] = self.request.user.id
            if not "contributeur" in request.data:
                request.data["contributeur"] = self.request.user.id            
            request.data_mutable = False
        serializer = serializers.ProjectCreationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            data["infos"] = "Votre projet a été créé"
            serializer.save()
        else:
            data["info"] = "Votre saisie comporte des erreurs"
        return Response(data=data)


class UserView(ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        IdUser = (self.request.user.id)
        # Crypte le mot de passe si il est indiqué lors d'une mise à jour
        if self.action == "partial_update" or self.action == "update":
            if ('password' in self.request.data):
                password_crypted = make_password(self.request.data['password'])
                self.request.data._mutable = True
                self.request.data["password"] = password_crypted
                self.request.data_mutable = False
            pass
        return models.User.objects.filter(id=IdUser)
       


class IssueView(ModelViewSet):
    serializer_class = serializers.IssueListSerializer
    detail_serializer_class = serializers.IssueDetailSerializer
    permission_classes = [IsAuthenticated & IsAuthor | IsProjectContributor]

    def get_queryset(self):
        return models.Issue.objects.all()

    # Suivant la requete, change le serializer
    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        else:
            return super().get_serializer_class()

    def create(self, request, format=None):
        # Affecte automatiquement l'auteur
        if request.data:
            request.data._mutable = True
            request.data["author"] = self.request.user.id
            request.data_mutable = False
        serializer = serializers.IssueCreationSerializer(data=request.data, many=True)
        data = {}
        if serializer.is_valid():
            data["infos"] = "Votre issue a été créée"
            serializer.save()
        else:
            data["info"] = "Votre saisie comporte des erreurs"
        return Response(data=data)


class IssueCommentView(ModelViewSet):
    serializer_class = serializers.IssueCommentListSerializer
    detail_serializer_class = serializers.IssueCommentDetailSerializer
    permission_classes = [IsAuthenticated & IsAuthor | IsProjectContributor ]

    def get_queryset(self):
        return models.IssueComment.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        else:
            return super().get_serializer_class()

    def create(self, request, format=None):
        # Affecte automatiquement l'auteur
        if request.data:
            request.data._mutable = True
            request.data["author"] = self.request.user.id
            request.data_mutable = False
        serializer = serializers.IssueCommentCreationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            data["infos"] = "Votre commentaire a été créée"
            serializer.save()
        else:
            data["info"] = "Votre saisie comporte des erreurs"
        return Response(data=data)


class InscriptionView(APIView):
    permission_classes = []
    serializer = serializers.UserCreationSerializer
      
    def post(self, request): 
        # Permet de crypter le mot de passe, si il est bien mis dans la requete
        if ('password' in self.request.data):
                password_crypted = make_password(self.request.data['password'])
                request.data._mutable = True
                request.data["password"] = password_crypted
                request.data_mutable = False

        serializer = self.serializer(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.save()
            data['infos'] = "Votre compte a été créer"
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data=data)
    
    def perform_create(self, serializer):
        # Hash password but passwords are not required
        if ('password' in self.request.data):
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()

