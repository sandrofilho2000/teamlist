from django import template

register = template.Library()

@register.filter(name='enshort_name')
def enshort_name(value):
    
    if len(value) > 20 :
        return "..."
    
    else:
        return value
    



