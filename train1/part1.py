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

# Print all red pixel coordinates
# for y, x in zip(red_y, red_x):
    # print(f"Red Pixel Coordinate: (y: {y}, x: {x})")

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

three_groups = []

# Find the top 10 columns with the most red pixels
top_columns = sorted(column_counts, key=column_counts.get, reverse=True)[:30]
for column in top_columns:
    three_groups.append(column)
    # print(f"The column {column} has {column_counts[column]} red pixels.")

    # Sort the three_groups array
    three_groups.sort()

    # Split the sorted array into three groups
    group_size = len(three_groups) // 3
    group1 = three_groups[:group_size]
    group2 = three_groups[group_size:2*group_size]
    group3 = three_groups[2*group_size:]
    
    group1 = group1[3:]
    group1 = group1[:-3]

    group2 = group2[3:]
    group2 = group2[:-3]

    group3 = group3[3:]
    group3 = group3[:-3]

group1_avg = sum(group1) / len(group1)
group2_avg = sum(group2) / len(group2)
group3_avg = sum(group3) / len(group3)

# print(three_groups)

# Print the three groups
# print("Group 1:", group1)
# print("Group 2:", group2)
# print("Group 3:", group3)

# Print the three groups
# print("Group 1:", group1_avg)
# print("Group 2:", group2_avg)
# print("Group 3:", group3_avg)

# Convert to 1 meter
# group 3 - group 1 = 1 meter
meter = group3_avg - group1_avg
# print(meter)
# conversion factor
conversion = 1000 / meter

os.system('python part2.py ' + sys.argv[1] + ' ' + str(conversion) + ' > part2.txt')

os.system('python part3.py > ' + sys.argv[1][:-4] + '.txt')


# red = bags[:,:,0]*mask
# green = bags[:,:,1]*mask
# blue = bags[:,:,2]*mask
# bags_masked = np.dstack((red,green,blue))

# imshow(bags_masked)

# plt.show()
