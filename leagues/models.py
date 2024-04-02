from django import forms
from django.db import models
from colorfield.fields import ColorField

from countries.models import Country

# Model for representing a league
class League(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=255, null=False, blank=False)
    link = models.CharField(verbose_name="Link", max_length=255, null=True, blank=True)
    small_img = models.CharField(verbose_name="Imagem pequena", max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=250, null=False, blank=False)  # Slug for SEO-friendly URLs
    img = models.CharField(verbose_name="Imagem", max_length=255, null=False, blank=False)
    outcomes = models.CharField(verbose_name="Despesas", max_length=20, null=False, blank=False)
    incomes = models.CharField(verbose_name="Renda", max_length=20, null=False, blank=False)
    balance = models.CharField(verbose_name="Saldo", max_length=20, null=False, blank=False)
    country_name = models.CharField(verbose_name="País", max_length=255, null=False, blank=False)
    country_img = models.CharField(verbose_name="País", max_length=255, null=False, blank=False)
    small_img = models.CharField(verbose_name="Bandeira do país", max_length=255, null=False, blank=False)
    background_color = ColorField(verbose_name="Cor de fundo (vazio para automático)", null=True)  
    text_color = ColorField(verbose_name="Cor do texto (vazio para automático)", null=True) 
    id_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Ligas"

# Form for updating league colors
class LeagueColorForm(forms.ModelForm):
    class Meta:
        model = League
        fields = ['text_color', 'background_color']
