import csv


def getPrediction(A,B):

    APV = {}
    BPV = {}

    for i in A:
        APV[i] = 0.1

    for i in B:
        BPV[i] = 0.1

    with open("Player_Values.csv", 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for line in reader:
                if line[0] in A:
                    APV[line[0]] = float(line[1])

                if line[0] in B:
                    BPV[line[0]] = float(line[1])

    Ta = sum(APV.values())
    Tb = sum(BPV.values())

    print("team A strength:\t" + str(Ta))
    print("team B strength:\t" + str(Tb))


    if Ta>Tb:

        WP = ((Ta)/(Ta+Tb))*100
        print("Winning % of A is" + "\t" + str(WP))
        print("Winning % of B is" + "\t" + str(100 - WP))

    else:

        WP = ((Tb) /(Ta+Tb)) * 100
        print("Winning % of B is" + "\t" + str(WP))
        print("Winning % of A is" + "\t" + str(100 - WP))




RCB = { 'CH Gayle', 'V Kohli','SR Watson',  'YS Chahal','P Negi','KM Jadhav','TM Head', 'AF Milne','S Aravind','STR Binny','Mandeep Singh'}

MI = {'R Sharma','JJ Bumrah','JC Buttler','SL Malinga','MJ McClenaghan','HH Pandya','KH Pandya','PA Patel','KA Pollard','N Rana','Harbajan Singh'}

GL = {'DR Smith','Ishan Kishan','BB McCullum','SK Raina','AJ Finch','RA Jadeja','KD Karthik','Shivil','AJ Tye','Basil Thampi','DS Kulkarni'}

DD = {'SV Samson', 'SS Iyer', 'KK Nair', 'J Yadav', 'RR Pant', 'SW Billings', 'Z Khan', 'A Mishra', 'PJ Cummins', 'AD Mathews','CH Morris'}

KKR =  {'SP Narine', 'G Gambhir', 'RV Uthappa', 'NM Coulter-Nile','MK Pandey', 'SA Yadav','UT Yadav', 'CR Woakes', 'Kuldeep Yadav', 'C de Grandhomme','YK Pathan'}

KXIP ={'M Vohra','GJ Maxwell','WP Saha','EJG Morgan','HM Amla','I Sharma','AR Patel','MM Sharma','KC Cariappa','Sandeep Sharma','DA Miller'}

SRH = {'DA Warner','S Dhawan','S Kaul','MC Henriques','Yuvraj Singh','DJ Hooda','NV Ojha', 'Rashid Khan','B Kumar','KS Williamson','Mohammed Siraj'}

RPS = {'AM Rahane','SPD Smith','JD Unadkat','MS Dhoni','BA Stokes','RD Chahar','RA Tripathi','MK Tiwary','DT Christian','SN Thakur','Imran Tahir'}

getPrediction(SRH ,DD)