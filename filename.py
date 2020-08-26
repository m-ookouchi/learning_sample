import sys
import re
import csv

if len(sys.argv) != 2 :
    print("[Usage]")
    print("    python " + sys.argv[0] + " csvfilename")
    sys.exit()

fileName = sys.argv[1]
# print(fileName)
table_name = fileName[:-4]

r = re.compile("^.*\.csv$")
if r.match(fileName) :
    #print("Extention is csv")
    pass
else:
    #print("Extention is not csv")
    sys.exit()

csvData = []
keys = set()
with open(fileName) as f :
    reader = csv.DictReader(f)
    for row in reader :
        # print(row)
        keys.update(row)
        csvData.append(row)
    f.close()

print("Table Name: " + table_name)
for key in keys:
    print("colimn '" + key + "' values : ", end="")
    for data in csvData:
        print(data[key] + ", ", end="")
    print("")

