import pandas as pd


Bat14 = pd.read_csv("Batting_2014.csv")
Bat15 = pd.read_csv("Batting_2015.csv")
Bat16 = pd.read_csv("Batting_2016.csv")
Bat17 = pd.read_csv("Batting_2017.csv")
Bow14 = pd.read_csv("Bowling_2014.csv")
Bow15 = pd.read_csv("Bowling_2015.csv")
Bow16 = pd.read_csv("Bowling_2016.csv")
Bow17 = pd.read_csv("Bowling_2017.csv")
BatI14 = pd.read_csv("T20I_Batting_2014.csv")
BatI15 = pd.read_csv("T20I_Batting_2015.csv")
BatI16 = pd.read_csv("T20I_Batting_2016.csv")
BatI17 = pd.read_csv("T20I_Batting_2017.csv")
BowI14 = pd.read_csv("T20I_Bowling_2014.csv")
BowI15 = pd.read_csv("T20I_Bowling_2015.csv")
BowI16 = pd.read_csv("T20I_Bowling_2016.csv")
BowI17 = pd.read_csv("T20I_Bowling_2017.csv")



Ba14 = {}
Ba15 = {}
Ba16 = {}
Ba17 = {}
Bo14 = {}
Bo15 = {}
Bo16 = {}
Bo17 = {}
BaI14 = {}
BaI15 = {}
BaI16 = {}
BaI17 = {}
BoI14 = {}
BoI15 = {}
BoI16 = {}
BoI17 = {}


FPV = {}
Batsmen = []
Bowlers = []


for i in range(Bat14['Batsman'].count()):
   Batsmen.append(Bat14['Batsman'].iloc[i])
   Ba14[Bat14['Batsman'].iloc[i]] = Bat14['Quantifier'].iloc[i]

for i in range(Bat15['Batsman'].count()):
   Ba15[Bat15['Batsman'].iloc[i]] = Bat15['Quantifier'].iloc[i]
   if Bat15['Batsman'].iloc[i] not in Batsmen:
       Batsmen.append(Bat15['Batsman'].iloc[i])

for i in range(Bat16['Batsman'].count()):
   Ba16[Bat16['Batsman'].iloc[i]] = Bat16['Quantifier'].iloc[i]
   if Bat16['Batsman'].iloc[i] not in Batsmen:
       Batsmen.append(Bat16['Batsman'].iloc[i])

for i in range(Bat17['Batsman'].count()):
   Ba17[Bat17['Batsman'].iloc[i]] = Bat17['Quantifier'].iloc[i]
   if Bat17['Batsman'].iloc[i] not in Batsmen:
       Batsmen.append(Bat17['Batsman'].iloc[i])

for i in range(BatI14['Batsman'].count()):
    BaI14[BatI14['Batsman'].iloc[i]] = BatI14['Quantifier'].iloc[i]
    if BatI14['Batsman'].iloc[i] not in Batsmen:
        Batsmen.append(BatI14['Batsman'].iloc[i])

for i in range(BatI15['Batsman'].count()):
    BaI15[BatI15['Batsman'].iloc[i]] = BatI15['Quantifier'].iloc[i]
    if BatI15['Batsman'].iloc[i] not in Batsmen:
        Batsmen.append(BatI15['Batsman'].iloc[i])

for i in range(BatI16['Batsman'].count()):
    BaI16[BatI16['Batsman'].iloc[i]] = BatI16['Quantifier'].iloc[i]
    if BatI16['Batsman'].iloc[i] not in Batsmen:
        Batsmen.append(BatI16['Batsman'].iloc[i])

for i in range(BatI17['Batsman'].count()):
    BaI17[BatI17['Batsman'].iloc[i]] = BatI17['Quantifier'].iloc[i]
    if BatI17['Batsman'].iloc[i] not in Batsmen:
        Batsmen.append(BatI17['Batsman'].iloc[i])




for i in range(Bow14['Bowler'].count()):
   Bowlers.append(Bow14['Bowler'].iloc[i])
   Bo14[Bow14['Bowler'].iloc[i]] = Bow14['Quantifier'].iloc[i]

for i in range(Bow15['Bowler'].count()):
   Bo15[Bow15['Bowler'].iloc[i]] = Bow15['Quantifier'].iloc[i]
   if Bow15['Bowler'].iloc[i] not in Bowlers:
       Bowlers.append(Bow15['Bowler'].iloc[i])

for i in range(Bow16['Bowler'].count()):
   Bo16[Bow16['Bowler'].iloc[i]] = Bow16['Quantifier'].iloc[i]
   if Bow16['Bowler'].iloc[i] not in Bowlers:
       Bowlers.append(Bow16['Bowler'].iloc[i])

for i in range(Bow17['Bowler'].count()):
   Bo17[Bow17['Bowler'].iloc[i]] = Bow17['Quantifier'].iloc[i]
   if Bow17['Bowler'].iloc[i] not in Bowlers:
       Bowlers.append(Bow17['Bowler'].iloc[i])

for i in range(BowI14['Bowler'].count()):
   BoI14[BowI14['Bowler'].iloc[i]] = BowI14['Quantifier'].iloc[i]
   if BowI14['Bowler'].iloc[i] not in Bowlers:
       Bowlers.append(BowI14['Bowler'].iloc[i])

for i in range(BowI15['Bowler'].count()):
   BoI15[BowI15['Bowler'].iloc[i]] = BowI15['Quantifier'].iloc[i]
   if BowI15['Bowler'].iloc[i] not in Bowlers:
       Bowlers.append(BowI15['Bowler'].iloc[i])

for i in range(BowI16['Bowler'].count()):
   BoI16[BowI16['Bowler'].iloc[i]] = BowI16['Quantifier'].iloc[i]
   if BowI16['Bowler'].iloc[i] not in Bowlers:
       Bowlers.append(BowI16['Bowler'].iloc[i])

for i in range(BowI17['Bowler'].count()):
   BoI17[BowI17['Bowler'].iloc[i]] = BowI17['Quantifier'].iloc[i]
   if BowI17 ['Bowler'].iloc[i] not in Bowlers:
       Bowlers.append(BowI17['Bowler'].iloc[i])



for i in Batsmen:

    FPV[i] =  []

    if i in Ba14.keys():
        FPV[i].append(Ba14[i])

    if i in Ba15.keys():
        FPV[i].append(Ba15[i])

    if i in Ba16.keys():
        FPV[i].append(Ba16[i])

    if i in Ba17.keys():
        FPV[i].append(Ba17[i])

    if i in BaI14.keys():
        FPV[i].append(BaI14[i])

    if i in BaI15.keys():
        FPV[i].append(BaI15[i])

    if i in BaI16.keys():
        FPV[i].append(BaI16[i])

    if i in BaI17.keys():
        FPV[i].append(BaI17[i])

FPVb = {}

for i in Bowlers:
    FPVb[i] =  []
    if i in Bo14.keys():
        FPVb[i].append(Bo14[i])

    if i in Bo15.keys():
        FPVb[i].append(Bo15[i])

    if i in Bo16.keys():
        FPVb[i].append(Bo16[i])

    if i in Bo17.keys():
        FPVb[i].append(Bo17[i])

    if i in BoI14.keys():
        FPVb[i].append(BoI14[i])

    if i in BoI15.keys():
        FPVb[i].append(BoI15[i])

    if i in BoI16.keys():
        FPVb[i].append(BoI16[i])

    if i in BoI17.keys():
        FPVb[i].append(BoI17[i])


players = list(set(Batsmen+ Bowlers))
BatVal = list(FPV.keys())

#print(FPV)
for each in BatVal:
    FPV[each] = float(sum(FPV[each])/len(FPV[each]))

#print("**************************************************************************")

print(FPV)

BowVal = list(FPVb.keys())
#print("**************************************************************")
#print(FPVb)
for each in BowVal:
    FPVb[each] = float(sum(FPVb[each]) / len(FPVb[each]))
#print("*******************************************************************************")
print(FPVb)

print(type(BowVal))
Final_Values = {}

for i in players:

    Final_Values[i] = 0

    if all([i in BatVal,i in BowVal]):
        Final_Values[i] = FPV[i] + FPVb[i]

    elif i in BatVal :
        Final_Values[i] = FPV[i]

    elif i in BowVal:
        Final_Values[i] = FPVb[i]

    else:
        print("Error")

#print("******************************************")
print(Final_Values)

import csv

with open('Player_Values.csv', 'a', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Player', 'Value']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    for i,j in Final_Values.items():
        writer.writerow({'Player': i, 'Value': j})


with open('Batsmen.csv', 'a', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Player', 'Value']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    for i,j in FPV.items():
        writer.writerow({'Player': i, 'Value': j})

with open('Bowlers.csv', 'a', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Player', 'Value']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    for i,j in FPVb.items():
        writer.writerow({'Player': i, 'Value': j})

Alrounders = {}

for i in FPV.keys():
    if i in FPVb.keys():
        Alrounders[i] = FPV[i] + FPVb [i]

with open('Alrounders.csv', 'a', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Player', 'Value']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    for i,j in Alrounders.items():
        writer.writerow({'Player': i, 'Value': j})