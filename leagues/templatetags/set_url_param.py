from xxlimited import new
from django import template

register = template.Library()

@register.filter(name='set_url_param')
def set_url_param(url = False):
    params = url.split("?")
    new_url = ""

    if len(params) == 1:
        new_url = "?"
    
    else: 
        if "?page=" in url:
            new_url = "?"
        
        elif "&page=" in url:
            params = params[-1].split("&page=")
            new_url = f"?{params[0]}&"
         
        else:
            new_url = f"?{params[-1]}&"
     
    return new_url