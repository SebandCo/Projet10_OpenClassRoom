from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .permissions import IsAuthor, IsContributor, IsProjectContributor, IsUser

from . import models
from . import serializers

class ProjectView(ModelViewSet):
    serializer_class = serializers.ProjectSerializer
    permission_classes=[IsAuthenticated, IsAuthor|IsContributor]

    def get_queryset(self):
        return models.Project.objects.all()
    
    def create(self,request, format=None):
        # Affecte automatiquement l'auteur et le contributeur
        if request.data:
            request.data._mutable = True
            request.data["author"] = self.request.user.id
            request.data["contributeur"] = self.request.user.id
            request.data_mutable = False
        serializer = serializers.ProjectSerializer(data=request.data)
        data ={}
        if serializer.is_valid():
            data["infos"] = "Votre projet a été créé"
            serializer.save()
        else:
            data["info"] = "Votre saisie comporte des erreurs"
        return Response(data=data)

class UserView(ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        IdUser=(self.request.user.id)
        return models.User.objects.filter(id=IdUser)
    
class IssueView(ModelViewSet):
    serializer_class = serializers.IssueSerializer
    permission_classes=[IsAuthenticated, IsAuthor|IsProjectContributor]
    
    def get_queryset(self):
        return models.Issue.objects.all()
    
    def create(self,request, format=None):
        # Affecte automatiquement l'auteur
        if request.data:
            request.data._mutable = True
            request.data["author"] = self.request.user.id
            request.data_mutable = False
        serializer = serializers.IssueSerializer(data=request.data)
        data ={}
        if serializer.is_valid():
            data["infos"] = "Votre issue a été créée"
            serializer.save()
        else:
            data["info"] = "Votre saisie comporte des erreurs"
        return Response(data=data)


class InscriptionView(APIView):
   
    def post(self, request, format=None):
        serializer = serializers.UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['infos'] = "Votre compte a été créer"
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data=data)



        

