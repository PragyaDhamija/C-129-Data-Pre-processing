import csv
dataset_1 = []
dataset_2 = []
with open("dataset_1.csv") as f:
    cd = csv.reader(f)
    for i in cd:
        dataset_1.append(i)
with open("dataset2_sorted.csv") as g:
    cd2 = csv.reader(g)
    for s in cd2:
        dataset_2.append(s)
headers_1 = dataset_1[0]
headers_2 = dataset_2[0]
planet_data1 = dataset_1[1:]
planet_data2 = dataset_2[1:]

header = headers_1 + headers_2
planet_data = []
for index,item in enumerate(planet_data1):
    planet_data.append(planet_data1[index] + planet_data2[index])

with open("final.csv","a+") as l:
    c = csv.writer(l)
    c.writerow(header)
    c.writerows(planet_data)
