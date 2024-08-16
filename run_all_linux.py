import os
import csv

file_dir = "patch_perfect_data//train_images"
file_list = os.listdir(file_dir)
print(len(file_list))
float_array = []
file_name_array = []

for file_name in file_list:
    if file_name.endswith(".jpg"):
        file_path = os.path.join(file_dir, file_name)
        file_name_array.append(file_name)
        print(file_name)
#         with open(file_path, "r") as file:
#             first_line = file.readline().strip()
#             try:
#                 float_value = float(first_line)
#                 float_array.append(float_value)
#             except ValueError:
#                 print(f"Invalid float value in file: {file_name}")
print(len(file_name_array))
# print(file_name_array)

# for file_name in file_name_array:
    # os.system("python part1.py " + file_dir + file_name)
