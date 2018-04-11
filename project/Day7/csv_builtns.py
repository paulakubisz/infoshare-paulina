import csv
import pprint

db = []

with open('osoby1.csv') as file:

    reader = csv.reader(file)

    for line in reader:
        db.append(line)



db.append([18,'Adam', 'Pilot', '40'])

pprint.pprint(db,indent=4)

with open('osoby1.csv', 'r+') as file:

    file.read()

    writer = csv.writer(file)
    writer.writerow(db[-1])