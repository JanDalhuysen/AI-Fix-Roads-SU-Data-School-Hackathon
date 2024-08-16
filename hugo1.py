import sys

from PIL import Image

def find_red_pixels(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Convert image to RGB mode if not already in that mode
        img = img.convert('RGB')
        # Load image data
        pixels = img.load()
        width, height = img.size
        
        red_pixels = []
        
        # Iterate through each pixel in the image
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                # Check if the pixel is red
                if r > 200 and g < 50 and b < 50:  # Adjust the threshold as needed
                    red_pixels.append((x, y))
        
        return red_pixels

# Example usage
image_path = 'C:/Apps/pothole/AI-Fix-Roads-SU-Data-School-Hackathon/patch_perfect_data/train_images/p166.jpg'
red_pixel_coordinates = sorted(find_red_pixels(image_path))
print(red_pixel_coordinates)

import matplotlib.pyplot as plt

# Plot the red pixel coordinates
x_coords, y_coords = zip(*red_pixel_coordinates)
plt.scatter(x_coords, y_coords, color='red')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Red Pixel Coordinates')
plt.show()