from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .permissions import IsAuthor, IsContributor

from . import models
from . import serializers

class ProjectView(ModelViewSet):
    serializer_class = serializers.ProjectSerializer
    permission_classes=[IsAuthenticated, IsAuthor|IsContributor]

    def get_queryset(self):
        return models.Project.objects.all()

class UserView(ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes=[IsAdminUser]

    def get_queryset(self):
        return models.User.objects.all()
    
class IssueView(ModelViewSet):
    serializer_class = serializers.IssueSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return models.Issue.objects.all()

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



        

