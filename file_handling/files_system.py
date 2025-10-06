import csv

data=[
     ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 24, 'London'],
    ['Charlie', 35, 'Paris']
    
]

csv_filename = 'my_data.csv'

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write each row of data
    writer.writerows(data)

print(f"CSV file '{csv_filename}' created successfully.")