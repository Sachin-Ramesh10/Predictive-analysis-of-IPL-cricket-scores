import csv

Bat = {}
Bow = {}
Allr = {}

BatIPL = {}
BowIPL = {}
AllrIPL = {}

with open("Batsmen.csv",'r') as f:
    reader = csv.reader(f, delimiter = ',')
    for line in reader:
        Bat[line[0]] = line[1]

with open("Bowlers.csv",'r') as f:
    reader = csv.reader(f, delimiter = ',')
    for line in reader:
        Bow[line[0]] = line[1]

with open("Alrounders.csv",'r') as f:
    reader = csv.reader(f, delimiter = ',')
    for line in reader:
        Allr[line[0]] = line[1]

with open("SampleValues.csv",'r') as f:
    reader = csv.reader(f, delimiter = ',')
    for line in reader:

         if line[0] in Bat.keys():
             BatIPL[line[0]] = Bat[line[0]]

         if line[0] in Bow.keys():
             BowIPL[line[0]] = Bow[line[0]]

         if line[0] in Allr.keys():
             AllrIPL[line[0]] = Allr[line[0]]


with open('IPLBatsmen.csv', 'a', newline='', encoding='UTF-8') as f:
        fieldnames = ['username', 'Values']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        for i, j in BatIPL.items():
            writer.writerow({'username': i, 'Values': j})

with open('IPLBowlers.csv', 'a', newline='', encoding='UTF-8') as f:
    fieldnames = ['username', 'Values']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    for i, j in BowIPL.items():
        writer.writerow({'username': i, 'Values': j})


with open('IPLAllrounders.csv', 'a', newline='', encoding='UTF-8') as f:
    fieldnames = ['username', 'Values']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    for i, j in AllrIPL.items():
        writer.writerow({'username': i, 'Values': j})