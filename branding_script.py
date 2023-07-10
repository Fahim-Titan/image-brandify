from PIL import Image
import os

# add folder location that contains all the images that needs branded logo
folder_path_a = ""
# Brand Logo folder path (must be in PNG format, must be named as logo.png)
folder_path_b = "D:\OneDrive\projects\Instagram_project_01\Logo"

def add_image_to_right_bottom_corner(image_path, overlay_image_path):
    overlay_image = Image.open(overlay_image_path).convert('RGBA')
    overlay_width, overlay_height = overlay_image.size

    original_image = Image.open(image_path).convert('RGBA')
    original_width, original_height = original_image.size

    # Calculate the size of the overlay image as 10% of the original image size
    overlay_size = int(original_width * 0.1)
    overlay_image = overlay_image.resize((overlay_size, overlay_size))

    # Create a new image with the same size as the original image
    new_image = Image.new("RGBA", (original_width, original_height))

    # Paste the original image onto the new image
    new_image.paste(original_image, (0, 0))

    # Calculate the coordinates to paste the overlay image at the bottom right corner
    overlay_x = original_width - overlay_size
    overlay_y = original_height - overlay_size

    # Paste the overlay image at the bottom right corner
    new_image.paste(overlay_image, (overlay_x, overlay_y), overlay_image)

    # Save the final image
    new_image.save(image_path)

for filename in os.listdir(folder_path_a):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(folder_path_a, filename)
        overlay_image_path = os.path.join(folder_path_b, "logo.png")
        add_image_to_right_bottom_corner(image_path, overlay_image_path)
