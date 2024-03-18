from django.contrib import admin
from .models import Team
from django.shortcuts import render, get_object_or_404
from django.contrib import admin

admin.site.site_header = "Sandro Filho DEV"

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'background_color', 'text_color']  # Adjusted list_display
    search_fields = ['name']  # Adjusted search_fields


    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Guest').exists():  # Assuming 'Guest' is the group name
            return [field.name for field in self.model._meta.fields if field.name not in ['background_color', 'text_color']]
        return super().get_readonly_fields(request, obj)