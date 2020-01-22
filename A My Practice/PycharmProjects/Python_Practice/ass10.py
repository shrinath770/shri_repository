import csv
row_list = [["SN", "Name", "City"],
            [1, "Shrinath Hattekar", "Nanded"],
            [2, "Jay Poul", "Parbhani"],
            [3, "Ananda Parve", "Nanded"]]
with open('shri.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

with open('shri.csv') as file:
    data=csv.reader(file)
    for row in data:
        print(row)
file.close()