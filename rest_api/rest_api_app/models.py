from django.db import models
from .status import STATUS_CHOICES


class Users(models.Model):
    email = models.EmailField(blank=False, unique=True)
    phone = models.IntegerField(blank=False, unique=True)
    fam = models.CharField(blank=False)
    name = models.CharField(blank=False)
    otc = models.CharField(blank=False)


class PerevalAdded(models.Model):
    beautyTitle = models.CharField(blank=False)
    title = models.CharField(blank=False)
    other_titles = models.CharField()
    connect = models.CharField()
    add_time = models.DateTimeField(auto_now_add=True)
    winter_lvl = models.CharField()
    summer_lvl = models.CharField()
    autumn_lvl = models.CharField()
    spring_lvl = models.CharField()
    coord_id = models.ForeignKey("Coordinates", on_delete=models.CASCADE)
    user_added = models.ForeignKey("Users", on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES)


class Activity(models.Model):
    name = models.CharField(blank=False)


class PerevalAreas(models.Model):
    id_parent = models.IntegerField()
    title = models.CharField()


class Coordinates(models.Model):
    latitude = models.CharField(blank=False)
    longitude = models.CharField(blank=False)
    height = models.IntegerField(blank=False)


class PerevalImages(models.Model):
    pereval_id = models.ForeignKey("PerevalAdded", on_delete=models.CASCADE)
    photo_id = models.CharField(blank=False)
