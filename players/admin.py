from django.contrib import admin
from players.models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth','country_name']  
    search_fields = ['name', 'birth','country_name']  

