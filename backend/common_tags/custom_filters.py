# custom_filters.py
from django import template
from datetime import datetime

register = template.Library()

@register.filter(name='passToFloat')
def passToFloat(value = 0):
    positive = 1
    
    if str(value).find("-") != -1:
        positive = -1
        value = value.replace("-", "") 
      
    try:
        value = float(value)

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
    
    except:
        return '-'
    
    
@register.filter(name='enshort_name')
def enshort_name(value):
    
    if len(value) > 23 :
        return value[:23] + "..."
    
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


@register.filter(name='set_country_pagination_params')
def set_country_pagination_params(request, tab = False):
    params = request.GET.dict()
    
    if not params['tab']:
        if tab!="leagues":
            return 'hidden'
        else: 
            return ''
        
    else:
        if params['tab'] == "leagues":
            if tab != "leagues":
                return 'hidden'
            
        elif params['tab'] == "teams":
            if tab != "teams":
                return 'hidden'
            
        elif params['tab'] == "players":
            if tab != "players":
                return 'hidden'
            
        return ""
    
    
@register.filter(name='get_stadium_img')
def get_stadium_img(src):
    
    if src:
        src = src.split("%%")
        return src[0]
    else:
        return "https://t4.ftcdn.net/jpg/04/17/36/11/360_F_417361125_RnrhT3Np0zB0UpeD7QlwuOoyghEGGjBX.jpg"
    
    
    
@register.filter(name='format_date_with_age')
def format_date_with_age(date_str):
    date_str = str(date_str).strip()

    if "/" in date_str:
        try:
            date = datetime.strptime(date_str, '%d/%m/%Y')
        except ValueError as e:
            print(f"Error parsing date: {e} {date_str}")
            return date_str
        
        today = datetime.today()
        age = today.year - date.year - ((today.month, today.day) < (date.month, date.day))
        
        formatted_date = f"{date_str} ({age})"
        
        return formatted_date
    else:
        return "-"
