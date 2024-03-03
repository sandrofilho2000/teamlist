# custom_filters.py
from django import template

register = template.Library()

@register.filter(name='passToFloat')
def passToFloat(value = 0):
    positive = 1
    
    if str(value).find("-") != -1:
        positive = -1
        value = value.replace("-", "") 
      
    try:
        value = float(value)
    except:
        print("VALOR: ", value)    
    
    if(value >= 1000000000):
        new_value =  value / 1000000000
        new_value = str(new_value * positive) + " bilhões €"
        return new_value
    
    elif(value >= 1000000):
        new_value =  value / 1000000
        new_value = str(new_value * positive) + " mi. €"
        return new_value
    
    elif(value >= 1000):
        new_value =  value / 1000
        new_value = str(new_value * positive) + " mil €"
        return new_value
    
    else:
        return "-"
    
    
@register.filter(name='enshort_name')
def enshort_name(value):
    
    if len(value) > 27 :
        return value[:27] + "..."
    
    else:
        return value
    
    
@register.simple_tag
def url_params(request):
    params = request.GET.dict()
    if 'page' in params:
        del params['page'] 
    if params:
        return '&' + '&'.join([f"{k}={v}" for k, v in params.items()])
    return ''


@register.filter(name='set_pagination_params')
def set_pagination_params(url = False):
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