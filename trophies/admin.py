from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Trophy
from django.shortcuts import render, get_object_or_404

@admin.register(Trophy)
class TrophyAdmin(admin.ModelAdmin):
    list_display = ['name']# Adjusted list_display
    search_fields = ['name']  # Adjusted search_fields
