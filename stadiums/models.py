from django.db import models

class Stadium(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    seats = models.IntegerField(default=0)
    build_year = models.CharField(max_length=255)
    grass_heat = models.CharField(max_length=255)
    grass_type = models.CharField(max_length=255)
    grass_size = models.CharField(max_length=255)
    imgs = models.CharField(max_length=255)
    staterooms = models.IntegerField(default=0)
    build_value = models.CharField(max_length=255)
    oficial_site = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    crowd_capacity = models.IntegerField(default=0)
    team_name= models.CharField(max_length=255)
        
    def __str__(self):
        return self.name



