from django.db import models

from django.db import models
from countries.models import Country
from teams.models import Team  # Assuming you have a Team model in the teams app

class Player(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    slug = models.CharField(max_length=255, null=True, blank=True)
    img = models.CharField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    pos = models.CharField(max_length=255, null=True, blank=True)
    id_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    id_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    num = models.CharField(max_length=255)
    birthdate = models.CharField(max_length=255)
    country_flag = models.CharField(max_length=255)
    country_name = models.CharField(max_length=255)
    value_market = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name
