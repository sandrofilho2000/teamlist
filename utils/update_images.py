import os
from PIL import Image

def convert_images_to_webp(folder_path):
    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        # Check if the file is a PNG image
        if os.path.isfile(file_path) and filename.lower().endswith('.png'):
            # Open the PNG image
            with Image.open(file_path) as img:
                # Construct the path for the WebP image
                webp_file_path = os.path.join(folder_path, os.path.splitext(filename)[0] + '.webp')
                # Convert and save the image as WebP
                img.save(webp_file_path, 'webp')
                print(f"Converted {filename} to WebP")
            # Delete the original PNG image
            os.remove(file_path)
            print(f"Deleted {filename}")

# Define the folder path
folder_path = 'media/images/teams'
folder_path_leagues = 'media/images/leagues'
folder_path_countries = 'media/images/countries'

# Call the function to convert images to WebP and delete PNGs
convert_images_to_webp(folder_path)
convert_images_to_webp(folder_path_leagues)
convert_images_to_webp(folder_path_countries)
