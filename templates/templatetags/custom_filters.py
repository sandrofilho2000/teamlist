from django import template

register = template.Library()

@register.filter(name='enshort_name')
def enshort_name(value):
    
    if len(value) > 20 :
        return "..."
    
    else:
        return value


@register.filter(name='get_text_color')
def get_text_color(item):
    if hasattr(item, 'text_color') and item.text_color:
        return item.text_color
    elif hasattr(item, 'league') and hasattr(item.league, 'text_color') and item.league.text_color:
        return item.league.text_color
    else:
        return None