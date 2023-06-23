from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .models import *
from .serializers import *


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    http_method_names = ['post']


class PerevalAddedViewSet(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer
    http_method_names = ['post', 'get']


class CoordinatesViewSet(viewsets.ModelViewSet):
    queryset = Coordinates.objects.all()
    serializer_class = CoordinatesSerializer
    http_method_names = ['post', 'patch']


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    http_method_names = ['post']


class PerevalAreasViewSet(viewsets.ModelViewSet):
    queryset = PerevalAreas.objects.all()
    serializer_class = PerevalAreasSerializer
    http_method_names = ['post']


class PerevalImagesViewSet(viewsets.ModelViewSet):
    queryset = PerevalImages.objects.all()
    serializer_class = PerevalImagesSerializer
    http_method_names = ['post']


@api_view(['PATCH'])
def pereval_added_patch_method(request, pk):
    try:
        pereval = PerevalAdded.objects.get(pk=pk)
    except PerevalAdded.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        if pereval.status != 'new':
            return Response({
                'state': 0,
                'message': "Failed to update pereval!"
            })
        serializer = PerevalChangedSerializer(pereval, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data)
            return Response({
                'state': 1,
                'message': "Successfully updated pereval!"
            })
        else:
            return Response({
                'state': 0,
                'message': f"{serializer.errors}"
            })


@api_view(["GET"])
def sort_pereval(request, email):
    try:
        current_user = Users.objects.get(email=email)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        perevals = PerevalAdded.objects.filter(user_added=current_user.pk).values('id', 'beautyTitle', 'title',
                                                                                  'other_titles', 'connect',
                                                                                  'winter_lvl', 'summer_lvl',
                                                                                  'autumn_lvl', 'spring_lvl',
                                                                                  'coord_id', 'status')
        return Response(perevals)