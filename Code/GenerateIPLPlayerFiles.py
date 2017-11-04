SRH = {'B Kumar	S Dhawan',	'B Kumar	MC Henriques', 'NV Ojha',	'Ricky Bhui',	'KS Williamson',	'S Kaul	Bipul Sharma',	'A Nehra',	'Yuvraj Singh',
        'BCJ Cutting',	'Abhimanyu Mithun',	'Mustafizur Rahman',	'BB Sran',	'DJ Hooda',	'V Shankar',	'CJ Jordan',	'Mohammad Nabi',	'Eklavya Dwivedi',
        'Rashid Khan','PV Tambe','Ben laughing',	'Tanmay Agarwal',	'Mohammed Siraj'}


RCB = {'A Choudhary	','AB de Villiers',	'AF Milne',	'CH Gayle',	'HV Patel'	,'KM Jadhav',	'Mandeep Singh',	'S Aravind',	'S Badree',	'Sachin Baby',
        'SR Watson',	'STR Binny',	'YS Chahal',	'SN Khan',	'Iqbal Abdulla',	'TM Head',	'Avesh khan',	'T Shamsi',	'P Negi',	'TS Mills','Praveen Dubey',
        'B Stanlake',	'Vishnu Vinod',	'V Kohli'}


PG = {'SPD Smith',	'SN Thakur',	'MS Dhoni',	'AM Rahane',	'F du Plessis',	'AB Dinda',	'Ankush Bains',	'R Bhatia',	'Ankit Sharma',	'IC Pandey',
        'A Zampa',	'Jaskaran Singh',	'Baba Aparajith',	'RD Chahar',	'DT Christian',	'LH Ferguson'	,'UT Khawaja',	'MA Agarwal',	'BA Stokes',	'MK Tiwary',
        'JD Unadkat',	'DL Chahar',	'Saurabh Kumar',	'Milind Tandon',	'RA Tripathi','Imran Tahir',	'Washington Sundar'}


MI = {'R Sharma','JJ Bumrah','JC Buttler','KV Sharma','MJ McClenaghan','HH Pandya','KH Pandya','PA Patel','KA Pollard','N Rana','SL Malinga', 'Harbajan Singh',
      'AT Rayudu','S Gopal','LMP Simmons', 'R Vinay Kumar','N Rana','Siddesh Lad','J Suchith','TG Southee','J Sharma','D Punia','SS Tiwary','N Pooran','MG Johnson'
      ,'KV Sharma','DAS Gunaratne','K Gowtham','K Khejroliya'}


KKR =  {'SP Narine', 'G Gambhir', 'RV Uthappa', 'S Jackson','MK Pandey', 'YK Pathan','C de Grandhomme', 'CR Woakes', 'NM Coulter-Nile', 'Kuldeep Yadav','UT Yadav',
        'AD Russell','SA Yadav','PP Chawla','Shakib Al Hasan','CA Lynn','AS Rajpoot','TA Boult','DM Bravo','R Dhawan','CR Woakes','R Powell','I Jaggi','S Ghosh',
        'RSS Yadav'}


KPU ={'M Vohra','MJ Guptill','WP Saha','VR Aaron','HM Amla','GJ Maxwell','AR Patel','MM Sharma','T Natarajan','Sandeep Sharma','SE Marsh','DA Miller','GS Mann',
      'Anureet Singh','NS Naik','MP Stoinis','KC Cariappa  ','A Jaffer','P Sahu','Swapnil Singh','EJG Morgan','MJ Henry','R Tewatia','DJG Sammy','Rinku Singh',
      'I Sharma'}


GL = {'JP Faulkner','Ishan Kishan','BB McCullum','SK Raina','AJ Finch','RA Jadeja','KD Karthik','PJ Sangwan','A soni','Basil Thampi','DR Smith','DS Kulkarni','P Kumar',
      'PJ Sangwan','SB Jakati','J Shah','Manpreet Goni','N Singh','JJ Roy','MM Patel','C Suri','AD Nath','S Agarwal','Tejas Baroka','P Singh','S Shaurya','IK Pathan'}


DD = {'SV Samson', 'K Rabada', 'KK Nair', 'SS Iyer', 'RR Pant', 'CJ Anderson', 'Mohammed Shami', 'A Mishra', 'J Yadav', 'AD Mathews','CH Morris','Z Khan','PJ Cummins',
      'Ankit Bawne','AP Tare','M Ashwin','S Saini','Shashank Singh','S Nadeem','SW Billings','CR Brathwaite','C Milind','K Ahmed','Prathyush Singh','BW Hilfenhaus',
      'MN Samuels'}



MIPV = {}
GLPV ={}
DDPV = {}
KKPV = {}
KPUPV ={}
RCBPV = {}
PGPV = {}
SRHPV = {}


for i in MI:
    MIPV[i] = 0.1

for i in GL:
    GLPV[i] = 0.1
for i in DD:
    DDPV[i] = 0.1

for i in KKR:
    KKPV[i] = 0.1

for i in KPU:
    KPUPV[i] = 0.1
	
for i in RCB:
    RCBPV[i] = 0.1

for i in SRH:
    SRHPV[i] = 0.1

for i in PG:
    PGPV[i] = 0.1

import csv

with open("Player_Values.csv",'r') as f:
    reader = csv.reader(f, delimiter = ',')
    for line in reader:

        if line[0] in GL:
            GLPV[line[0]] = float(line[1])

        if line[0] in KKR:
            KKPV[line[0]] = float(line[1])

        if line[0] in DD:
            DDPV[line[0]] = float(line[1])

        if line[0] in KPU:
            KPUPV[line[0]] = float(line[1])

        if line[0] in SRH:
            SRHPV[line[0]] = float(line[1])
			        if line[0] in DD:
            DDPV[line[0]] = float(line[1])

        if line[0] in RCB:
            RCBPV[line[0]] = float(line[1])

        if line[0] in PG:
            PGPV[line[0]] = float(line[1])

with open('IPLALLPlayersList.csv', 'a', newline='', encoding='UTF-8') as f:
        fieldnames = ['username', 'Values']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writerow({'username': "Gujarath Lions", 'Values': ""})
        for i,j in GLPV.items():
            writer.writerow({'username': i, 'Values': j})

        writer.writerow({'username': "Kolkata knight Riders", 'Values': ""})
        for i,j in KKPV.items():
            writer.writerow({'username': i, 'Values': j})

        writer.writerow({'username': "Mumbai Indians", 'Values': ""})
        for i,j in MIPV.items():
            writer.writerow({'username': i, 'Values': j})

        writer.writerow({'username': "Delhi DareDevils", 'Values': ""})
        for i,j in DDPV.items():
            writer.writerow({'username': i, 'Values': j})

        writer.writerow({'username': "Kings XI", 'Values': ""})
        for i,j in KPUPV.items():
            writer.writerow({'username': i, 'Values': j})
			
	    writer.writerow({'username': "Gujarath Lions", 'Values': ""})
        for i,j in GLPV.items():
            writer.writerow({'username': i, 'Values': j})

        writer.writerow({'username': "SunRisers Hyderabad", 'Values': ""})
        for i,j in SRHPV.items():
            writer.writerow({'username': i, 'Values': j})

        writer.writerow({'username': "Royal Challengers Bengaluru", 'Values': ""})
        for i,j in RCBPV.items():
            writer.writerow({'username': i, 'Values': j})

        writer.writerow({'username': "Rising Pune Super Giants", 'Values': ""})
        for i,j in PGPV.items():
            writer.writerow({'username': i, 'Values': j})
