import os
import requests
from pickletools import float8
import sys
from turtle import pos
import re

from slugify import slugify

# Add the root directory of your Django project to the Python path
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from sql_commands import *





    
    
    
def download_image(folder="", img_url="", save_name=""):
    save_folder = r"C:\xampp\htdocs\Not legacy\Python\Futeapp\static\images\{FOLDER}"
    save_folder.replace("{FOLDER}", folder)
    # Create the folder if it doesn't exist
    os.makedirs(save_folder, exist_ok=True)

    # Get the image content from the URL
    response = requests.get(img_url)
    if response.status_code == 200:
        # Construct the file path
        save_path = os.path.join(save_folder, save_name)

        # Write the image content to the file
        with open(save_path, 'wb') as file:
            file.write(response.content)
        
        print(f"Image downloaded and saved as '{save_name}' in '{save_folder}'.")
    else:
        print(f"Failed to download image from '{img_url}'. Status code: {response.status_code}")
        


    
