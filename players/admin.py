from django.contrib import admin
from players.models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'birthdate','country_name']  
    search_fields = ['name', 'birthdate','country_name']  

