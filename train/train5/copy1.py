import os
import csv

# file_dir = "C:/Apps/pothole/train3/"
file_dir = "C:/Apps/pothole/AI-Fix-Roads-SU-Data-School-Hackathon/patch_perfect_data/test_images/"
# file_dir = "C:/Apps/pothole/AI-Fix-Roads-SU-Data-School-Hackathon/train/train5/"
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

area_numbags_file = "area_numbags.csv"
train_labels_file = "train_labels.csv"

# with open(area_numbags_file, "w", newline="") as area_numbags_csv:
    # writer = csv.writer(area_numbags_csv)
    # for i in range(len(float_array)):
        # writer.writerow([float_array[i], file_name_array[i]])

# print("Done writing to area_numbags.csv")

# error ----------------------------------------------------------------------------------------------------

found_counter = 0
not_found_counter = 0
total_counter = 0

with open(train_labels_file, "r") as train_labels_csv:
    reader = csv.reader(train_labels_csv)
    for row in reader:
        total_counter += 1

        if 'p'+row[0]+'.txt' in file_name_array:
            print('p'+row[0]+'.txt')
            found_counter += 1
        else:
            print('p'+row[0]+'.txt not found')
            not_found_counter += 1

# print("found counter : " + str(found_counter))
# print("not found counter : " + str(not_found_counter))
# print("total counter : " + str(total_counter))

# error ----------------------------------------------------------------------------------------------------

        with open(area_numbags_file, "a", newline="") as area_numbags_csv:
            writer = csv.writer(area_numbags_csv)
            print(len(file_name_array))
            print(len(float_array))
            for i in range(len(file_name_array)):
                if file_name_array[i] == 'p'+row[0]+'.txt':
                    print("Index : " + str(i))
                    print("Float : " + str(float_array[i]))
                    print("File name : " + file_name_array[i])
                    print("Bags used : " + row[1])
                    writer.writerow([float_array[i], row[1]])
                





                # writer.writerow(['a', 'b'])
                # print("flaot arr : " + float_array[int(row[0])])
                # writer.writerow([float_array[int(row[0])], row[1]])


                # find which index in the file_name_array is equal to the row[0]
                # print("Row : " + row[0])
