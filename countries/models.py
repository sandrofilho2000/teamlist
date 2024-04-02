from colorfield.fields import ColorField
from django import forms
from django.db import models

# Define the Country model
class Country(models.Model):
    name = models.CharField(
        verbose_name="Nome", max_length=255, null=False, blank=False
    )
    slug = models.CharField(
        verbose_name="Slug", max_length=255, null=False, blank=False
    )
    flag = models.CharField(
        verbose_name="Bandeira", max_length=255, null=False, blank=False
    )
    background_color = ColorField(verbose_name="Cor de fundo (vazio para automático)", null=True)  
    text_color = ColorField(verbose_name="Cor do texto (vazio para automático)", null=True)   
    
    # String representation of the object
    def __str__(self):
        return self.name
    
    # Integer representation of the object
    def __int__(self):
        return self.pk

    class Meta:
        verbose_name_plural = "Países"
        verbose_name = "País"
        ordering = ["name"]
    
# Define the form for updating Country colors
class CountryColorForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['text_color', 'background_color']
