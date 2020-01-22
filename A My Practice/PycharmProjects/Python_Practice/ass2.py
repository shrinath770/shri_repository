import csv

file=open('/home/shri/Downloads/data.csv')
data=csv.reader(file)
for row in data:
    print(row)
file.close()