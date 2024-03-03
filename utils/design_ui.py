from PIL import Image
from collections import Counter

def get_most_common_colors(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Convert the image to RGB mode
        img = img.convert("RGB")
        # Resize the image to reduce processing time
        img.thumbnail((200, 200))

        # Get pixel colors
        colors = list(img.getdata())

        # Count the occurrence of each color
        color_counter = Counter(colors)

        # Get the four most common colors
        most_common_colors = color_counter.most_common(10)

        # Convert RGB colors to RGB format
        rgb_colors = [rgb for rgb, _ in most_common_colors]

        return rgb_colors

# Example usage:
image_path = r"C:\xampp\htdocs\Not legacy\Python\Futeapp\static\images\leagues\liga-de-expansion-mx-clausura157.png"
colors = get_most_common_colors(image_path)





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
        
        if diff < -40 or diff > 40:
            new_colors.append(curr_color)

    new_colors = sorted(new_colors, key=lambda x: sum(x))
    return new_colors
  
    



def calculate_contrast(color1, color2):
    # Calculate the luminance of color1
    luminance1 = (0.2126 * color1[0] / 255) + (0.7152 * color1[1] / 255) + (0.0722 * color1[2] / 255)

    # Calculate the luminance of color2
    luminance2 = (0.2126 * color2[0] / 255) + (0.7152 * color2[1] / 255) + (0.0722 * color2[2] / 255)

    # Calculate the contrast ratio
    contrast_ratio = (max(luminance1, luminance2) + 0.05) / (min(luminance1, luminance2) + 0.05)

    return contrast_ratio



def select_colors(colors):
    max_contrast_ratio = 0
    selected_colors = None

    if len(colors) == 3:
        background_color = colors[1]
        text_color = colors[2]
        if sum(background_color) >= 382:
            text_color = colors[0]
    
    elif len(colors) == 4:
        background_color = colors[1]
        text_color = colors[2]
        if sum(background_color) >= 382:
            text_color = colors[0]
        
    else:
        background_color = colors[1]
        text_color = colors[2]
        if sum(background_color) >= 382:
            text_color = colors[0]
        
   

    return {"background_color": f"rgb{background_color}", "text_color": f"rgb{text_color}"}

# Example usage:
removed_duplicated_colors = remove_duplicate_colors(colors)
selected_colors = select_colors(removed_duplicated_colors)
print("Removed duplicated colors:", removed_duplicated_colors)
print("Selected colors:", selected_colors)
