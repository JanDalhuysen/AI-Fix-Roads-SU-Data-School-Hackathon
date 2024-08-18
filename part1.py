from skimage.io import imread, imshow
from skimage.color import rgb2hsv
import numpy as np
import matplotlib.pyplot as plt

import sys
import os

bags = imread(sys.argv[1])

bags_hsv = rgb2hsv(bags)
fig, ax = plt.subplots(1, 1, figsize=(12,4))

#refer to hue channel (in the colorbar)
lower_mask = bags_hsv[:,:,0] > 0.0
#refer to hue channel (in the colorbar)
upper_mask = bags_hsv[:,:,0] < 0.05

#refer to transparency channel (in the colorbar)
saturation_mask = bags_hsv[:,:,1] > 0.4

mask = upper_mask*lower_mask*saturation_mask

# Find red pixel coordinates (y, x)
red_y, red_x = np.where(mask == True)

final_x = []
final_y = []

# plt.show()
# for x,y in zip(red_x, red_y):
    # print(str(x) + " " + str(y))

for x,y in zip(red_x, red_y):
    count = 0
    for a,b in zip(red_x, red_y):
        if(x == a and y == b):
            continue

        dist = np.sqrt((x-a)**2 + (y-b)**2)

        if(dist < 5):
            count+=1
    
    if(count>15):  #sus
        final_x.append(x)
        final_y.append(y)


#DSU
n = len(final_x)

e = [-1 for i in range(n)]

def find(v):
    if(e[v]<0):
        return v
    else:
        e[v]=find(e[v])
        return e[v]
    
def join(a,b):
    a=find(a)
    b=find(b)

    if(a==b):
        return 0

    if(e[a]>e[b]):
        temp=a
        a=b
        b=temp
    
    e[a]+=e[b]
    e[b]=a
    return 1



for i in range(n):
    for j in range(n):
        dist = (final_x[i]-final_x[j])**2+(final_y[i]-final_y[j])**2

        if(dist<40):  #sus
            join(i,j)
        
leaders = []

for i in range(n):
    if(e[i]<0):
        leaders.append(i)

groups_x = []
groups_y = []
groups = []

for i in range(len(leaders)):
    temp_x= []
    temp_y = []
    temp = []
    for j in range(n):
        if(find(j)==leaders[i]):
            temp.append(j)
            temp_x.append(final_x[j])
            temp_y.append(final_y[j])
    
    groups.append(temp)
    groups_x.append(temp_x)
    groups_y.append(temp_y)

# for j in groups:
    # print(j)

    # print()
    # print()

print(len(groups))

group_sizes = [len(group) for group in groups]
count = sum(size > 50 for size in group_sizes)
print(f"There are {count} groups with more than 50 points.")

groups_x_avg = []
groups_y_avg = []

for group in groups:
    avg_x = np.mean([final_x[i] for i in group])
    print(f"Average x value of group: {avg_x}")
    groups_x_avg.append(avg_x)

for group in groups:
    avg_y = np.mean([final_y[i] for i in group])
    print(f"Average y value of group: {avg_y}")
    groups_y_avg.append(avg_y)

# Print the average x and y values of each group
for i in range(len(groups)):
    print(f"Group {i+1} - Average (x, y): ({groups_x_avg[i]}, {groups_y_avg[i]})")

# Check if there are any groups very close to another
close_groups = []
for i in range(len(groups)):
    for j in range(i+1, len(groups)):
        dist = np.sqrt((groups_x_avg[i] - groups_x_avg[j])**2 + (groups_y_avg[i] - groups_y_avg[j])**2)
        if dist < 50:  # Adjust the threshold as needed
            close_groups.append((i, j))

if len(close_groups) > 0:
    print("There are groups that are very close to each other:")
    for group1, group2 in close_groups:
        print(f"Group {group1+1} and Group {group2+1}")
else:
    print("There are no groups that are very close to each other.")

# Remove close groups
new_groups = []
for i in range(len(groups)):
    is_close = False
    for j in range(i+1, len(groups)):
        dist = np.sqrt((groups_x_avg[i] - groups_x_avg[j])**2 + (groups_y_avg[i] - groups_y_avg[j])**2)
        if dist < 50:  # Adjust the threshold as needed
            is_close = True
            break
    if not is_close:
        new_groups.append(groups[i])

# Update groups and groups_x_avg, groups_y_avg
groups = new_groups
groups_x_avg = [np.mean([final_x[i] for i in group]) for group in groups]
groups_y_avg = [np.mean([final_y[i] for i in group]) for group in groups]

# Print the updated groups
for i in range(len(groups)):
    print(f"Group {i+1} - Average (x, y): ({groups_x_avg[i]}, {groups_y_avg[i]})")

conversion = 0

if len(groups) == 2:
    group1_x_avg, group1_y_avg = groups_x_avg[0], groups_y_avg[0]
    group2_x_avg, group2_y_avg = groups_x_avg[1], groups_y_avg[1]
    distance_between_groups = np.sqrt((group1_x_avg - group2_x_avg)**2 + (group1_y_avg - group2_y_avg)**2)
    print(f"The distance between the two groups is {distance_between_groups} pixels.")
    conversion = 500 / distance_between_groups

if len(groups) == 3:
    group1_x_avg, group1_y_avg = groups_x_avg[0], groups_y_avg[0]
    group2_x_avg, group2_y_avg = groups_x_avg[1], groups_y_avg[1]
    group3_x_avg, group3_y_avg = groups_x_avg[2], groups_y_avg[2]
    distance_between_group1_and_group2 = np.sqrt((group1_x_avg - group2_x_avg)**2 + (group1_y_avg - group2_y_avg)**2)
    distance_between_group2_and_group3 = np.sqrt((group2_x_avg - group3_x_avg)**2 + (group2_y_avg - group3_y_avg)**2)
    distance_between_group1_and_group3 = np.sqrt((group1_x_avg - group3_x_avg)**2 + (group1_y_avg - group3_y_avg)**2)
    print(f"The distance between the first and second groups is {distance_between_group1_and_group2} pixels.")
    print(f"The distance between the second and third groups is {distance_between_group2_and_group3} pixels.")
    print(f"The distance between the first and third groups is {distance_between_group1_and_group3} pixels.")
    
    if abs(distance_between_group1_and_group2 + distance_between_group2_and_group3 - distance_between_group1_and_group3) < 10:  # Adjust the threshold as needed
        print("The sum of distances between groups 1 and 2, and groups 2 and 3 is close to the distance between groups 1 and 3.")
        conversion = 1000 / distance_between_group1_and_group3
    else:
        print("The sum of distances between groups 1 and 2, and groups 2 and 3 is not close to the distance between groups 1 and 3.")
        # Find the two groups that are closest to each other
        distances = [(distance_between_group1_and_group2, 1, 2), (distance_between_group2_and_group3, 2, 3), (distance_between_group1_and_group3, 1, 3)]
        distances.sort()
        print(f"Groups {distances[0][1]} and {distances[0][2]} are the closest to each other.")
        # Get the distance between the two closest groups
        distance_between_closest_groups = distances[0][0]
        print(f"The distance between the two closest groups is {distance_between_closest_groups} pixels.")
        conversion = 500 / distance_between_closest_groups

if len(groups) != 2 and len(groups) != 3:
    # Find the two largest groups
    largest_groups = sorted(groups, key=len, reverse=True)[:2]
    
    # Calculate the average (x, y) values of the largest groups
    largest_groups_x_avg = [np.mean([final_x[i] for i in group]) for group in largest_groups]
    largest_groups_y_avg = [np.mean([final_y[i] for i in group]) for group in largest_groups]

    # Print the average (x, y) values of the two largest groups
    for i in range(2):
        print(f"Group {i+1} - Average (x, y): ({largest_groups_x_avg[i]}, {largest_groups_y_avg[i]})")
    
    # Calculate the distance between the two largest groups
    distance_between_largest_groups = np.sqrt((largest_groups_x_avg[0] - largest_groups_x_avg[1])**2 + (largest_groups_y_avg[0] - largest_groups_y_avg[1])**2)
    
    print(f"The distance between the two largest groups is {distance_between_largest_groups} pixels.")
    conversion = 500 / distance_between_largest_groups

print(f"The conversion factor is {conversion}.")



# plt.scatter(final_x[0], final_y[0], color='red', s=1)
# plt.scatter(final_x[1], final_y[1], color='blue', s=1)
# plt.scatter(final_x[2], final_y[2], color='green', s=1)
# zip(red_y, red_x)
# Plot the red pixels on the image
# plt.scatter(red_x, red_y, color='red', s=1)
# plt.imshow(bags)
# plt.show()


os.system('python part2.py ' + sys.argv[1] + ' ' + str(conversion) + ' > part2.txt')

os.system('python part3.py > ' + sys.argv[1][:-4] + '.txt')
