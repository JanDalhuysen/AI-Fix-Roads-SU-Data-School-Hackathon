file_path = 'part2.txt'
target_line = 'Total'

result = []

with open(file_path, 'r') as file:
    for line in file:
        if line.startswith(target_line):
            result.append(line.strip())

# total area = width * height
# print(result[0][12:])
meters_squared = float(result[0][12:])/1000000
print(meters_squared)
