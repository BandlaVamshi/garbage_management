from __future__ import unicode_literals

from django.db import models

# Create your models here.
class data(models.Model):#Stores information about vehicles
    city_name      = models.CharField(max_length=200,default=None)
    city_latitude  = models.FloatField(default=None)#latitude of vehicle
    city_longitude = models.FloatField(default=None)#longitude of vehicle
    sensor1 = models.CharField(max_length = 200)
    sensor2 = models.CharField(max_length = 200)
    sensor3 = models.CharField(max_length = 200)
    def __str__(self):
        return str("data")
