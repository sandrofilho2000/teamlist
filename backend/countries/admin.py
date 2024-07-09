from django.contrib import admin

from countries.models import Country

@admin.register(Country)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name'] 
    search_fields = ['name', 'slug']  
    
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Guests').exists():  # Assuming 'Guest' is the group name
            return [field.name for field in self.model._meta.fields if field.name not in ['background_color', 'text_color']]
        return super().get_readonly_fields(request, obj)