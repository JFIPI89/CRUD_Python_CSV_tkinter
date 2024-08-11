import csv
import os

data_dir = 'database'

headers = {
    'items.csv': ['SKU', 'Name', 'Brand', 'Model', 'Department', 'Class', 'Family', 'Quantity', 'Stock', 'Discontinued'],
    'departments.csv': ['Department'],
    'classes.csv': ['Class', 'Department'],
    'families.csv': ['Family', 'Class', 'Department']
}

for file_name, header in headers.items():
    file_path = os.path.join(data_dir, file_name)
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
