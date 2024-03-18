from django.db import models
from colorfield.fields import ColorField
from django import forms

from countries.models import Country
from stadiums.models import Stadium

class Team(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    small_img = models.URLField(max_length=255)  # Assuming it's a URL
    average_market_value = models.FloatField(null=True, blank=True)
    total_market_value = models.FloatField(null=True, blank=True)
    country_name = models.CharField(max_length=255)
    country_img = models.URLField(max_length=255)  # Assuming it's a URL
    background_color = ColorField(verbose_name="Cor de fundo (vazio para automático)", null=True)  
    text_color = ColorField(verbose_name="Cor do texto (vazio para automático)", null=True)       
    id_stadium = models.ForeignKey(Stadium, verbose_name="Stadium", on_delete=models.SET_NULL, null=True, blank=True)
    id_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Equipes"
        verbose_name = 'Equipe'
    
    def __str__(self):
        return self.name
    
    def __int__(self):
        return self.pk

class TeamColorForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['text_color', 'background_color']
    
