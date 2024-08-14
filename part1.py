from skimage.io import imread, imshow
from skimage.color import rgb2hsv
import numpy as np
import matplotlib.pyplot as plt

import sys
import os

bags = imread(sys.argv[1])

bags_hsv = rgb2hsv(bags)
fig, ax = plt.subplots(1, 3, figsize=(12,4))

#refer to hue channel (in the colorbar)
lower_mask = bags_hsv[:,:,0] > 0.0
#refer to hue channel (in the colorbar)
upper_mask = bags_hsv[:,:,0] < 0.05

#refer to transparency channel (in the colorbar)
saturation_mask = bags_hsv[:,:,1] > 0.4

mask = upper_mask*lower_mask*saturation_mask

# Find red pixel coordinates (y, x)
red_y, red_x = np.where(mask == True)

# Count the number of red pixels in each y row
row_counts = {}
for y in red_y:
    if y in row_counts:
        row_counts[y] += 1
    else:
        row_counts[y] = 1

# Find the y row with the most red pixels
max_row = max(row_counts, key=row_counts.get)
# print(f"The y row with the most red pixels is {max_row} with {row_counts[max_row]} red pixels.")

# Count the number of red pixels in each x column
column_counts = {}
for x in red_x:
    if x in column_counts:
        column_counts[x] += 1
    else:
        column_counts[x] = 1

# Count the number of red pixels in each y row
row_counts = {}
for y in red_y:
    if y in row_counts:
        row_counts[y] += 1
    else:
        row_counts[y] = 1


# three_groups = []

most_popular_row = []

# Find the top 50 rows with the most red pixels
top_rows = sorted(row_counts, key=row_counts.get, reverse=True)[:50]
for row in top_rows:
    most_popular_row.append(row)
    # print(f"The row {row} has {row_counts[row]} red pixels.")

    # Sort the most_popular_row array
    most_popular_row.sort()

print("most popular rows")
print(most_popular_row)

most_popular_column = []

# Find the top 50 columns with the most red pixels
top_columns = sorted(column_counts, key=column_counts.get, reverse=True)[:50]
for column in top_columns:
    most_popular_column.append(column)
    # print(f"The column {column} has {column_counts[column]} red pixels.")

    # Sort the most_popular_column array
    most_popular_column.sort()

print("most popular columns")
print(most_popular_column)

# Find the pixel with the most red pixels around it in a radius of the standard deviation
# Calculate the standard deviation of the red pixel values
red_std = np.std(bags[:,:,0])

# Initialize variables to store the maximum count and corresponding pixel coordinates
max_count = 0
max_pixel = None

# Iterate over each red pixel
for y, x in zip(red_y, red_x):
    # Calculate the distance between the current pixel and all other red pixels
    distances = np.sqrt((red_y - y)**2 + (red_x - x)**2)
    
    # Count the number of red pixels within the standard deviation radius
    count = np.sum(distances <= red_std)
    
    # Update the maximum count and corresponding pixel coordinates if necessary
    if count > max_count:
        max_count = count
        max_pixel = (y, x)

# Print the pixel with the most red pixels around it
print(f"The pixel with the most red pixels around it is at (y: {max_pixel[0]}, x: {max_pixel[1]}) with {max_count} red pixels.")

point_one_x = max_pixel[1]
point_one_y = max_pixel[0]

second_max_count = 0
second_max_pixel = None

# Iterate over each red pixel
for y, x in zip(red_y, red_x):
    # Calculate the distance between the current pixel and point_one
    distance = np.sqrt((y - point_one_y)**2 + (x - point_one_x)**2)
    
    # Check if the distance is greater than 100 pixels
    if distance > 100:
        # Calculate the number of red pixels within the standard deviation radius
        count = np.sum(np.sqrt((red_y - y)**2 + (red_x - x)**2) <= red_std)
        
        # Update the second maximum count and corresponding pixel coordinates if necessary
        if count > second_max_count:
            second_max_count = count
            second_max_pixel = (y, x)

# Print the second pixel with the most red pixels around it
print(f"The second pixel with the most red pixels around it, more than 100 pixels away from point_one, is at (y: {second_max_pixel[0]}, x: {second_max_pixel[1]}) with {second_max_count} red pixels.")


point_two_x = second_max_pixel[1]
point_two_y = second_max_pixel[0]

# Calculate the distance between the two points
distance = np.sqrt((point_two_y - point_one_y)**2 + (point_two_x - point_one_x)**2)

# Print the distance between the two points
print(f"The distance between the two points is {distance} pixels.")
print(sys.argv[1])

# Calculate the conversion factor
conversion = 500 / distance

# Convert to 1 meter
# group 3 - group 1 = 1 meter
# meter = group3_avg - group1_avg
# print(meter)
# conversion factor
# conversion = 1000 / meter

os.system('python part2.py ' + sys.argv[1] + ' ' + str(conversion) + ' > part2.txt')

os.system('python part3.py > ' + sys.argv[1][:-4] + '.txt')

# red = bags[:,:,0]*mask
# green = bags[:,:,1]*mask
# blue = bags[:,:,2]*mask
# bags_masked = np.dstack((red,green,blue))

# imshow(bags_masked)

# plt.show()
