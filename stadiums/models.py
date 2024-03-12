from django.db import models

class Stadium(models.Model):
    name = models.CharField(max_length=255)
    grass_type = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    imgs = models.CharField(max_length=455)
    crowd_capacity = models.IntegerField(default=0)
    staterooms = models.IntegerField(default=0)
    build_value = models.FloatField(default=0)
