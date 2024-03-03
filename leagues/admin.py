from django.contrib import admin

from .models import League


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    
    list_display = [
        "name",
        "outcomes",
        "incomes",
        "balance",
        "country_name",
        "background_color",
        "text_color"
    ]  
    
    search_fields = [
        "name",
        "outcomes",
        "incomes",
        "balance",
        "country_name",
        "country_img",
        "small_img",
    ]
    
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Guest').exists():  # Assuming 'Guest' is the group name
            return [field.name for field in self.model._meta.fields if field.name not in ['background_color', 'text_color']]
        return super().get_readonly_fields(request, obj)
