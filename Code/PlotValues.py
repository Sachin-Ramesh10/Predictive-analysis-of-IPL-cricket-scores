import csv
import pandas as pd
from pylab import *

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

Batsmen = {}
Bowler = {}

with open('IPLBatsmen.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        Batsmen[line[0]] = line[1]

with open('IPLBowlers.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        Bowler[line[0]] = line[1]

SBat = list(sorted(Batsmen.values(), reverse=True))[:10]
SBow = list(sorted(Bowler.values(), reverse=True))[:10]

TopBat = {}
TopBow = {}

for i in SBat[:10]:
    TopBat[list(Batsmen.keys())[list(Batsmen.values()).index(i)]] = i

for i in SBow[:10]:
    TopBow[list(Bowler.keys())[list(Bowler.values()).index(i)]] = i

bat = {}
bow = {}

for player in TopBat.keys():
    print(player)
    k = {}
    k[2014] = 0.0
    k[2015] = 0.0
    k[2016] = 0.0
    k[2017] = 0.0

    for i in range(Bat14['Batsman'].count()):
        if Bat14['Batsman'].iloc[i] == player:
            k[2014] = k[2014] + float(Bat14['Quantifier'].iloc[i])

    for i in range(BatI14['Batsman'].count()):
        if BatI14['Batsman'].iloc[i] == player:
            k[2014] = k[2014] + float(BatI14['Quantifier'].iloc[i])

    for i in range(Bat15['Batsman'].count()):
        if Bat15['Batsman'].iloc[i] == player:
            k[2015] = k[2015] + float(Bat15['Quantifier'].iloc[i])

    for i in range(BatI15['Batsman'].count()):
        if BatI15['Batsman'].iloc[i] == player:
            k[2015] = k[2015] + float(BatI15['Quantifier'].iloc[i])

    for i in range(Bat16['Batsman'].count()):
        if Bat16['Batsman'].iloc[i] == player:
            k[2016] = k[2016] + float(Bat16['Quantifier'].iloc[i])

    for i in range(BatI16['Batsman'].count()):
        if BatI16['Batsman'].iloc[i] == player:
            k[2016] = k[2016] + float(BatI16['Quantifier'].iloc[i])

    for i in range(Bat17['Batsman'].count()):
        if Bat17['Batsman'].iloc[i] == player:
            k[2017] = k[2017] + float(Bat17['Quantifier'].iloc[i])

    for i in range(BatI17['Batsman'].count()):
        if BatI17['Batsman'].iloc[i] == player:
            k[2017] = k[2017] + float(BatI17['Quantifier'].iloc[i])

    bat[player] = k

for player in TopBow.keys():
    print(player)
    k = {}
    k[2014] = 0.0
    k[2015] = 0.0
    k[2016] = 0.0
    k[2017] = 0.0

    for i in range(Bow14['Bowler'].count()):
        if Bow14['Bowler'].iloc[i] == player:
            k[2014] = k[2014] + float(Bow14['Quantifier'].iloc[i])

    for i in range(BowI14['Bowler'].count()):
        if BowI14['Bowler'].iloc[i] == player:
            k[2014] = k[2014] + float(BowI14['Quantifier'].iloc[i])

    for i in range(Bow15['Bowler'].count()):
        if Bow15['Bowler'].iloc[i] == player:
            k[2015] = k[2015] + float(Bow15['Quantifier'].iloc[i])

    for i in range(BowI15['Bowler'].count()):
        if BowI15['Bowler'].iloc[i] == player:
            k[2015] = k[2015] + float(BowI15['Quantifier'].iloc[i])

    for i in range(Bow16['Bowler'].count()):
        if Bow16['Bowler'].iloc[i] == player:
            k[2016] = k[2016] + float(Bow16['Quantifier'].iloc[i])

    for i in range(BowI16['Bowler'].count()):
        if BowI16['Bowler'].iloc[i] == player:
            k[2016] = k[2016] + float(BowI16['Quantifier'].iloc[i])

    for i in range(Bow17['Bowler'].count()):
        if Bow17['Bowler'].iloc[i] == player:
            k[2017] = k[2017] + float(Bow17['Quantifier'].iloc[i])

    for i in range(BowI17['Bowler'].count()):
        if BowI17['Bowler'].iloc[i] == player:
            k[2017] = k[2017] + float(BowI17['Quantifier'].iloc[i])

    bow[player] = k

BT = list(bat.values())
BTn = list(bat.keys())
BBn = list(bow.keys())
BB = list(bow.values())

x = ['2014','2015','2016','2017']

B0 = [BT[0][2014],BT[0][2015],BT[0][2016],BT[0][2017]]
B1 = [BT[1][2014],BT[1][2015],BT[1][2016],BT[1][2017]]
B2 = [BT[2][2014],BT[2][2015],BT[2][2016],BT[2][2017]]
B3 = [BT[3][2014],BT[3][2015],BT[3][2016],BT[3][2017]]
B4 = [BT[4][2014],BT[4][2015],BT[4][2016],BT[4][2017]]
B5 = [BT[5][2014],BT[5][2015],BT[5][2016],BT[5][2017]]
B6 = [BT[6][2014],BT[6][2015],BT[6][2016],BT[6][2017]]
B7 = [BT[7][2014],BT[7][2015],BT[7][2016],BT[7][2017]]
B8 = [BT[8][2014],BT[8][2015],BT[8][2016],BT[8][2017]]
B9 = [BT[9][2014],BT[9][2015],BT[9][2016],BT[9][2017]]

plot(x,B0, label= BTn[0])
plot(x,B1, label= BTn[1])
plot(x,B2,label= BTn[2])
plot(x,B3,label= BTn[3])
plot(x,B4,label= BTn[4])
plot(x,B5,label= BTn[5])
plot(x,B6,label= BTn[6])
plot(x,B7,label= BTn[7])
plot(x,B8,label= BTn[8])
plot(x,B9,label= BTn[9])


xlabel('Year')
ylabel('Total Value')
title('Top Batsmen Performance over 4 years')
grid(True)
legend()
show()

BO0 = [BB[0][2014],BB[0][2015],BB[0][2016],BB[0][2017]]
BO1 = [BB[1][2014],BB[1][2015],BB[1][2016],BB[1][2017]]
BO2 = [BB[2][2014],BB[2][2015],BB[2][2016],BB[2][2017]]
BO3 = [BB[3][2014],BB[3][2015],BB[3][2016],BB[3][2017]]
BO4 = [BB[4][2014],BB[4][2015],BB[4][2016],BB[4][2017]]
BO5 = [BB[5][2014],BB[5][2015],BB[5][2016],BB[5][2017]]
BO6 = [BB[6][2014],BB[6][2015],BB[6][2016],BB[6][2017]]
BO7 = [BB[7][2014],BB[7][2015],BB[7][2016],BB[7][2017]]
BO8 = [BB[8][2014],BB[8][2015],BB[8][2016],BB[8][2017]]
BO9 = [BB[9][2014],BB[9][2015],BB[9][2016],BB[9][2017]]

plot(x,BO0, label= BBn[0])
plot(x,BO1, label= BBn[1])
plot(x,BO2,label= BBn[2])
plot(x,BO3,label= BBn[3])
plot(x,BO4,label= BBn[4])
plot(x,BO5,label= BBn[5])
plot(x,BO6,label= BBn[6])
plot(x,BO7,label= BBn[7])
plot(x,BO8,label= BBn[8])
plot(x,BO9,label= BBn[9])

xlabel('Year')
ylabel('Total Value')
title('Top Bowlers Performance over 4 years')
grid(True)
legend()
show()