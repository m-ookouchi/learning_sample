import csv
import json

filename = "sample.csv"

categories = []

with open(filename) as f:
    lines = csv.DictReader(f)

    print(type(lines))
    print(lines)

    for row in lines:
        print(row['ID'], row['name'])
        categories.append(row['name'])    
f.close()

for i in categories:
    print(i)
