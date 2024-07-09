from django.contrib import admin
from stadiums.models import Stadium

@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = ['name']  
    search_fields = ['name', 'slug']  