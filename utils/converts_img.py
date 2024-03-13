import os
from PIL import Image

def convert_to_webp_and_delete_png(folder_path):
    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):
            # Load the image
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)
            
            # Convert to WebP format
            webp_path = os.path.splitext(img_path)[0] + ".webp"
            img.save(webp_path, "WEBP")
            
            # Delete the PNG version
            os.remove(img_path)
            print(f"Converted {filename} to WebP and deleted the PNG version.")

if __name__ == "__main__":
    # Define the folder path
    teams_folder_path = os.path.join("..", "media", "teams")
    
    # Call the function
    convert_to_webp_and_delete_png(r"media\images\countries")
    convert_to_webp_and_delete_png(r"media\images\leagues")
    convert_to_webp_and_delete_png(r"media\images\system")
