from django.db import models
from colorfield.fields import ColorField
from django import forms

from countries.models import Country
from stadiums.models import Stadium

class Team(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    small_img = models.CharField(max_length=255)
    average_market_value = models.FloatField(null=True, blank=True)
    total_market_value = models.FloatField(null=True, blank=True)
    country_name = models.CharField(max_length=255)
    country_img = models.CharField(max_length=255)
    background_color = ColorField(verbose_name="Cor de fundo (vazio para automático)", null=True)  
    text_color = ColorField(verbose_name="Cor do texto (vazio para automático)", null=True)       
    id_stadium = models.ForeignKey(Stadium, verbose_name =("stadiums_stadium"), on_delete=models.SET_NULL, null=True, blank=True)
    id_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __int__(self):
        return self.pk
    
    def __str__(self):
        return self.name

class TeamColorForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['text_color', 'background_color']
        
    
