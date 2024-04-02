from django.db import models
from colorfield.fields import ColorField
from django import forms
from countries.models import Country
from stadiums.models import Stadium

class Team(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    img = models.URLField(max_length=255)  # URL for team image
    average_market_value = models.FloatField(null=True, blank=True)
    total_market_value = models.FloatField(null=True, blank=True)
    country_name = models.CharField(max_length=255)  # Name of the country
    country_img = models.URLField(max_length=255)  # URL for country flag image
    background_color = ColorField(verbose_name="Cor de fundo (vazio para automático)", null=True)  # Background color field
    text_color = ColorField(verbose_name="Cor do texto (vazio para automático)", null=True)  # Text color field
    id_stadium = models.ForeignKey(Stadium, verbose_name="Stadium", on_delete=models.SET_NULL, null=True, blank=True)
    id_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)  # Foreign key to country model
    
    class Meta:
        verbose_name = 'Equipe'  # Singular name for the model
        verbose_name_plural = "Equipes"  # Plural name for the model
        ordering = ['name']  # Default ordering by team name

    def __str__(self):
        return self.name  # String representation of the team model
    
    def __int__(self):
        return self.pk  # Integer representation of the team model (primary key)

class TeamColorForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['text_color', 'background_color']  # Form fields for text color and background color
