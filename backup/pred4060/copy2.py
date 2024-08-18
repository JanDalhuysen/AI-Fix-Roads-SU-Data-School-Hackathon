import os
import csv

# file_dir = "C:/Apps/pothole/train3/"
file_dir = "C:/Apps/newpothole/AI-Fix-Roads-SU-Data-School-Hackathon/pred4060/"
file_list = os.listdir(file_dir)
print(len(file_list))
float_array = []
file_name_array = []

for file_name in file_list:
    if file_name.endswith(".txt"):
        file_path = os.path.join(file_dir, file_name)
        file_name_array.append(file_name)
        with open(file_path, "r") as file:
            first_line = file.readline().strip()
            try:
                float_value = float(first_line)
                float_array.append(float_value)
            except ValueError:
                print(f"Invalid float value in file: {file_name}")

print(len(file_name_array))
print(len(float_array))

print(file_name_array)
print(float_array)

for i in range(len(file_name_array)):
    print(file_name_array[i][1:-4])
    print(",")
    os.system("learn_linear.exe " + str(float_array[i]))
    print("")
