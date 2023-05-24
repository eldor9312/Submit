from django.shortcuts import render
from rest_framework import viewsets

from .models import Users, PerevalAdded, Coordinates, PerevalImages, PerevalAreas, Activity
from .serializers import UsersSerializer, PerevalAddedSerializer, CoordinatesSerializer, PerevalImagesSerializer,\
    PerevalAreasSerializer, ActivitySerializer


class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    http_method_names = ['post']


class PerevalAddedViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer
    http_method_names = ['post']


class CoordinatesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Coordinates.objects.all()
    serializer_class = CoordinatesSerializer
    http_method_names = ['post']


class PerevalImagesViewSet(viewsets.ModelViewSet):
    queryset = PerevalImages.objects.all()
    serializer_class = PerevalImagesSerializer
    http_method_names = ['post']


class PerevalAreasViewSet(viewsets.ModelViewSet):
    queryset = PerevalAreas.objects.all()
    serializer_class = PerevalAreasSerializer
    http_method_names = ['post']


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    http_method_names = ['post']
