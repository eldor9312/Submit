from django.db import models
from rest_api_app.status import STATUS_CHOICES


class Users(models.Model):
    email = models.CharField(unique=True,blank=True)
    phone = models.IntegerField(unique=True,blank=False)
    fam = models.CharField(blank=False)
    name = models.CharField(blank=False)
    otc = models.CharField(blank=False)


class PerevalAdded(models.Model):
    beauty_title = models.CharField(blank=False)
    title = models.CharField(blank=False)
    other_titles = models.CharField()
    connect = models.CharField()
    add_time = models.DateTimeField()
    winter_lvl = models.CharField()
    summer_lvl = models.CharField()
    autumn_lvl = models.CharField()
    spring_lvl = models.CharField()
    coord_id = models.ForeignKey('Coordinates',on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES)
    creator = models.ForeignKey('Users',on_delete=models.CASCADE)

    # def update(instance, *args, **kwargs):
    #     if instance.status == 'New':
    #         print('lol')


class Coordinates(models.Model):
    latitude = models.CharField(blank=False)
    longtitude = models.CharField(blank=False)
    height = models.CharField(blank=False)


class PerevalImages(models.Model):
    pereval_id = models.ForeignKey(PerevalAdded,on_delete=models.CASCADE)
    photo_id = models.CharField()


class PerevalAreas(models.Model):
    parent_id = models.IntegerField(default=0)
    title = models.CharField(blank=False)


class Activity(models.Model):
    name = models.CharField(blank=False)
# Create your models here.
