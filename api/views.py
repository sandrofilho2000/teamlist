from turtle import color
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from collections import Counter
import os

from countries.models import Country


def rgb_to_hex(rgb):
    hex_color = '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
    return hex_color


def get_most_common_colors(folder, image_filename):


    return ""
    

def remove_duplicate_colors(colors):
    colors = sorted(colors, key=lambda x: sum(x))
    new_colors = []
    
    for i in range(0, len(colors)):
        if i == 0:
            last_color = colors[-1]
            curr_color = colors[0]
        else:
            last_color = colors[i - 1]
            curr_color = colors[i]
            
        last_red = last_color[0]
        last_green = last_color[1]
        last_blue = last_color[2]
        
        curr_red = curr_color[0]
        curr_green = curr_color[1]
        curr_blue = curr_color[2]
        
        diff = (last_red - curr_red) + (last_green - curr_green) + (last_blue - curr_blue)
        
        if diff < -20 or diff > 20:
            new_colors.append(curr_color)

    new_colors = sorted(new_colors, key=lambda x: sum(x))
    return new_colors
  
@api_view(['GET'])
def getDesignUi(request):
    folder = request.query_params.get('folder')
    img_name = request.query_params.get('img_name')
    colors = get_most_common_colors(folder, img_name)
    colors = remove_duplicate_colors(colors)

    print(colors)
    
    if len(colors) >=5:
        background_color = colors[2]
        if sum(background_color) < 300:
            text_color = colors[-1]
            
        else:
            background_color = colors[1]
            if sum(background_color) < 200:
                text_color = colors[-2]
            else:
                text_color = colors[-1]
    
    elif len(colors) == 4:
        if sum(colors[0]) > 10:
            background_color = colors[0]
            if sum(background_color) < 300:
                text_color = colors[-1]
                
            else:
                text_color = colors[-1]
            
        else:
            background_color = colors[1]
            if sum(background_color) < 154 and sum(colors[-2]) > 120:
                text_color = colors[-2]
            else:
                text_color = colors[-1]
                

            
    else:
        text_color = colors[-1]
        if sum(colors[0]) > 100 and sum(colors[-1]) > 500:
            background_color = colors[0]
            text_color = colors[-1]
        elif sum(colors[0]) == 0 and sum(colors[-1]) > 700:
            background_color = colors[1]
            if sum(colors[1]) < 500:
                text_color = colors[-1]
            else:
                text_color = (20, 20, 20)
        else:
            background_color = colors[0]
    
        
    print({"background_color": f"{rgb_to_hex(background_color)}", "text_color": f"{rgb_to_hex(text_color)}"})
   
    return Response({"background_color": f"{rgb_to_hex(background_color)}", "text_color": f"{rgb_to_hex(text_color)}"})


@api_view(['GET'])
def country_counts(request):
    # Get the query parameters from the request URL
    field = request.query_params.get('field')
    page = request.query_params.get('page')

    # Set default values for first_index and last_index
    first_index = 0
    last_index = 30

    if page:
        first_index = (int(page) - 1) * 30
        last_index = int(page) * 30



    countries = Country.objects.all().order_by(field)[first_index:last_index]
    counts = []
    for country in countries:
        counts.append({
            'name': country.slug,
            'num_teams': country.team_set.count(),
            'num_players': country.player_set.count(),
            'num_leagues': country.league_set.count(),
        })

    return Response({'counts': counts})