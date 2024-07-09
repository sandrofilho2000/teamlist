import os
from rest_framework.response import Response
from rest_framework.decorators import api_view
from PIL import Image
from countries.models import Country
from collections import Counter

# Function to convert RGB color to hexadecimal color
def rgb_to_hex(rgb):
    hex_color = '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
    return hex_color

# Function to get the most common colors in an image
def get_most_common_colors(folder, image_filename):
    # Open the image file
    image_path = os.path.join("media", "images", folder, image_filename)
    with Image.open(image_path) as img:
        # Convert the image to RGB mode
        img = img.convert("RGB")
        # Resize the image to reduce processing time
        img.thumbnail((200, 200))

        # Get pixel colors
        colors = list(img.getdata())

        # Count the occurrence of each color
        color_counter = Counter(colors)

        # Get the ten most common colors
        most_common_colors = color_counter.most_common(10)

        # Extract RGB values from the most common colors
        rgb_colors = [rgb for rgb, _ in most_common_colors]

        return rgb_colors

# Function to remove duplicate colors
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
        
        # Calculate the difference in RGB values
        diff = (last_red - curr_red) + (last_green - curr_green) + (last_blue - curr_blue)
        
        # If the difference is significant, add the color to the list of new colors
        if diff < -20 or diff > 20:
            new_colors.append(curr_color)

    new_colors = sorted(new_colors, key=lambda x: sum(x))
    
    if new_colors:
        return new_colors
    else:
        # If no new colors found, add default colors
        colors.append((255, 255, 255))
        colors.append((24, 24, 27))
        return colors
  
# API view to get design UI colors
@api_view(['GET'])
def getDesignUi(request):
    folder = request.query_params.get('folder')
    img_name = request.query_params.get('img_name')
    colors = get_most_common_colors(folder, img_name)
    colors = remove_duplicate_colors(colors)
    
    # Logic to determine background and text colors based on the image colors
    if len(colors) >= 5:
        background_color = colors[2]
        if sum(background_color) < 300:
            text_color = colors[-1]
        else:
            background_color = colors[1]
            if sum(background_color) < 200:
                text_color = colors[-2]
            else:
                text_color = colors[-1]
    
    # Handle case when there are exactly 4 colors
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
                
    # Handle case when there are less than 4 colors
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
    
    # Print and return the background and text colors
    print({"background_color": f"{rgb_to_hex(background_color)}", "text_color": f"{rgb_to_hex(text_color)}"})
    return Response({"background_color": f"{rgb_to_hex(background_color)}", "text_color": f"{rgb_to_hex(text_color)}"})

# API view to get country counts
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

    # Get countries from the database based on the specified field
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
