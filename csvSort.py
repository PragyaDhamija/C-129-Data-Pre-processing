import csv
data = []
with open("dataset_2.csv", "r") as f:
    c = csv.reader(f)
    for i in c:
        data.append(i)
header = data[0]
planet_data = data[1:]
for s in planet_data:
    s[2] = s[2].lower()
planet_data.sort(key=lambda planet_data:planet_data[2])

with open("dataset2_sorted.csv", "a+") as g:
    cd = csv.writer(g)
    cd.writerow(header)
    cd.writerows(planet_data)