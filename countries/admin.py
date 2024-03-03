from django.contrib import admin

from countries.models import Country

@admin.register(Country)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name']  # Campos a serem exibidos na lista de itens do painel admin
    search_fields = ['name']  # Campos que podem ser pesquisados no painel admin
