from rest_framework.response import Response

from .models import *
from rest_framework import serializers


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'email', 'phone', 'fam', 'name', 'otc']


class PerevalAddedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = ['id', 'beautyTitle', 'title', 'other_titles', 'connect', 'winter_lvl', 'summer_lvl', 'autumn_lvl',
                  'spring_lvl', 'user_added', 'coord_id', 'status']


class CoordinatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coordinates
        fields = ['id', 'latitude', 'longitude', 'height']


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'name']


class PerevalAreasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PerevalAreas
        fields = ['id', 'id_parent', 'title']


class PerevalImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PerevalImages
        fields = ['id', 'pereval_id', 'photo_id']


class PerevalChangedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = ['beautyTitle', 'title', 'other_titles', 'connect', 'winter_lvl', 'summer_lvl', 'autumn_lvl',
                  'spring_lvl']
