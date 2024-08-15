import os
import csv

# file_dir = ".\\patch_perfect_data\\train_images\\"
file_dir = ".\\patch_perfect_data\\test_images\\"
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

for file_name in file_name_array:
    print(f"Processing file: {file_name}")
    os.system("python part1.py " + file_dir + file_name)

# import os

# os.system("python part1.py .\\patch_perfect_data\\test_images\\p103.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p104.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p1040.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p105.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p108.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p1086.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p1115.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p1134.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p114.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p1161.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p1162.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p1181.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p1198.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p1205.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p1250.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p1270.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p1278.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p1280.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p1296.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p1409.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p143.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p1430.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p1438.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p144.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p406.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p434.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p450.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p470.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p473.jpg")
# os.system("python part1.py .\\patch_perfect_data\\test_images\\p479.jpg")
