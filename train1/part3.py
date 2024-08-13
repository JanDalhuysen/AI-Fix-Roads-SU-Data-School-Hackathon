file_path = 'part2.txt'
target_line = 'Total'

result = []

with open(file_path, 'r') as file:
    for line in file:
        if line.startswith(target_line):
            result.append(line.strip())

# total area = width * height
print(result[0][12:])
