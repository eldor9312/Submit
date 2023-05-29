from rest_framework import serializers
from .models import PerevalAdded, Users, Coordinates, PerevalImages, PerevalAreas, Activity


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['id','email','phone','fam','name','otc']


class PerevalAddedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = ['id','beauty_title','title','other_titles','connect','add_time','winter_lvl','summer_lvl','autumn_lvl','spring_lvl','coord_id','status','creator']


class CoordinatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coordinates
        fields = ['id', 'latitude', 'longtitude','height']


class PerevalImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PerevalImages
        fields = ['id','pereval_id','photo_id',]


class PerevalAreasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PerevalAreas
        fields = ['id','parent_id','title']


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ['id','name']

class PerevalChangedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = ['beautyTitle', 'title', 'other_titles', 'connect', 'winter_lvl', 'summer_lvl', 'autumn_lvl',
                  'spring_lvl']




