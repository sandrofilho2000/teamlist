from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TeamTrophy
from django.shortcuts import render, get_object_or_404

@admin.register(TeamTrophy)
class TeamTrophyAdmin(admin.ModelAdmin):
    list_display = ['id_team', 'id_trophy', 'season']# Adjusted list_display
    search_fields = ['season']  # Adjusted search_fields
