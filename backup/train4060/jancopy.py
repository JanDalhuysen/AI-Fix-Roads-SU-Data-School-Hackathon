import csv
import os

# Function to read the first line from a text file
def read_first_line(filename):
    with open(filename, 'r') as file:
        return file.readline().strip()

# Function to find the bags used for a given pothole number
def find_bags_used(pothole_number, labels):
    for row in labels:
        if row['Pothole number'] == pothole_number:
            return row['Bags used']
    return None

# Read the train_labels.csv file
with open('train_labels.csv', 'r') as file:
    labels = list(csv.DictReader(file))

# Prepare the output data
output_data = []

# Process each text file
for filename in os.listdir('.'):
    if filename.startswith('p') and filename.endswith('.txt'):
        pothole_number = filename[1:-4]  # Extract the number from the filename
        area = read_first_line(filename)
        
        # Look up the bags used from train_labels.csv
        bags_used = find_bags_used(pothole_number, labels)
        
        if bags_used is not None:
            output_data.append([pothole_number, area, bags_used])

# Sort the output data by pothole number
output_data.sort(key=lambda x: int(x[0]))

# Write the output to a new CSV file
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Pothole number', 'Area', 'Bags used'])
    writer.writerows(output_data)

print("Output CSV file has been created successfully.")
