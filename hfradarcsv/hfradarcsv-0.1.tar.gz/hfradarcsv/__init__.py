import os
import csv
from pathlib import Path
import datetime
Path.cwd()
import pandas as pd
now = datetime.datetime.now()
#print("Make sure there is no other File in the path except .tuv file only ")

def diagRDT():
    en_pa = str(input("Kindly Enter path of files Example for Mac: /Users/codar/Desktop/Jena sir Report/Totals GUCO/ for Windows 'C:\\Users\\Al\\spam' Else 1 for Default path: "))
    pat = False
    if en_pa == '1':
        en_pa = "/Users/codar/Desktop/Kalpakkam_Interference_Issue/"  # default path
        path = en_pa
        os.chdir(path)
    else:
        #print("Entered else")
        while pat == False:
            #print("Entered while")
            try:
                #print("Entered try")
                win_dir = Path(en_pa)
                win_dir.exists()
                pat = True
                os.chdir(en_pa)
                path = en_pa
            except:
                pat = False
                #print("Entered Ezxcept")
                en_pa = input(" Kindly Enter valid path: ")
                continue
            
    def RmSpaceConvertFloat(x):
        return float(x.strip())


    def RmSpace(x):
        return x.strip()

    results = []
    # keep only files with extesnion .rdt
    results += [each for each in os.listdir(path) if each.endswith('.rdt')]
    row=[]
    rows=[]
    #print(results)
    count=0
    for k in results:
        # print(i[10:20:1])
        #date = k[10:20:1].split('_')[0] + "-" + k[10:20:1].split('_')[1] + "-" + k[10:20:1].split('_')[2]
        sitecode = k[5:9:1]
        helloFile = open(path + k)
        helloContent = helloFile.readlines()
        StopCount = helloContent.index('%TableEnd:\n')
        # 31st line from top is the useful data for us
        for a in range(31, StopCount - 1):
            res = helloContent[a].split('  ')
            ch = [ele for ele in res if ele.strip()]
            #print(ch)
            nf1=ch[6].split('.')[0]
            #nf1=int(ch[7].split('.')[0])
            nf2=ch[6].split('.')[1]
            nf3=ch[6].split('.')[2]
            sn1=ch[7].split('.')[0]
            sn2=ch[7].split('.')[0]
            sn3=ch[7].split('.')[0]
            Vector_count=ch[11]
            max_range=ch[14]
            vel_max=ch[15]
            vel_avg=ch[16]
            #time:
            hour=ch[-1][0:2:1]
            mins=ch[-1][3:5:1]
            day=ch[-2][9:11:1]
            month=ch[-2][6:8:1]
            year=ch[-2][1:5:1]
            count += 1
            timestamp=year+"-"+month+"-"+day+" "+hour+":"+mins
            row=(timestamp+"," +nf1+"," +nf2+"," +nf3+"," +sn1+"," +sn2+"," +sn3+"," +Vector_count+"," +max_range+"," +vel_max+"," +vel_avg).split(',')
            #print(row)
            rows.append(row)
            helloFile.close()
            ch = ""
            nf2=""
            nf3=""
            sn1=""
            sn2=""
            sn3=""
            Vector_count=""
            max_range=""
            vel_max=""
            vel_avg=""
            #print(timestamp)
            #velocity = RmSpaceConvertFloat(ch[-4])
            #CurrentDirection = RmSpaceConvertFloat(ch[-3])
            #time = k[21:25:1]
            #dateTime=date+" "+time[0:2:1]+":"+time[2:4:1]
            #Long = ch[0]
            #lat = ch[1]
            #count += 1
            #row = (str(count) +"," +date +"," +time +","+Long +"," +lat +","+dateTime+","+str(velocity)+","+str(CurrentDirection)+","+sitecode).split(',')  # create row for CSV
            # print(k)
            #print(row)  # block it
            #rows.append(row)
            #ch = ""       
    fields = ['Time Stamp','nf1','nf2','nf3','sn1','sn2','sn3','vector count','max range','max Velocity (cm/s)','avg Velocity (cm/s)','SiteCode']
    filename = "ZDiagnostic_vector"+"_"+now.strftime("%Y_%m_%d_%H%M%S")+".csv"

    #with open(filename, 'w') as csvfile:
        # creating a csv writer object
        #csvwriter = csv.writer(csvfile)

        # writing the fields
        #csvwriter.writerow(fields)

        # writing the data rows
        #csvwriter.writerows(rows)
    #print("Wait........")
    print(" File is Saved as: "+ filename+" Saved in Path: "+ path)
    df = pd.DataFrame(rows)
    df.columns = ['Time Stamp','nf1','nf2','nf3','sn1','sn2','sn3','vector count','max range','max Velocity (cm/s)','avg Velocity (cm/s)']
    df.head()
    cols = df.columns.drop('Time Stamp')
    df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
    week_grouped = df.groupby(['Time Stamp']).mean().round(1)
    week_grouped.to_csv(sitecode+'_Diagnostic_Data_rdt'+"_"+now.strftime("%Y_%m_%d_%H%M%S")+".csv")

def totals():
    en_pa = str(input("Kindly Enter path of files Example for Mac: /Users/codar/Desktop/Jena sir Report/Totals GUCO/ for Windows 'C:\\Users\\Al\\spam' Else 1 for Default path: "))
    pat = False
    if en_pa == '1':
        en_pa = "/Users/codar/Desktop/Jena sir Report/Totals GUCO/"  # default path
        path = en_pa
        os.chdir("/Users/codar/Desktop/Jena sir Report/Totals GUCO/")
    else:
        #print("Entered else")
        while pat == False:
            #print("Entered while")
            try:
                #print("Entered try")
                win_dir = Path(en_pa)
                win_dir.exists()
                pat = True
                os.chdir(en_pa)
                path = en_pa
            except:
                pat = False
                #print("Entered Ezxcept")
                en_pa = input(" Kindly Enter valid path: ")
                continue
    """
    else:
        while pat == False:
            win_dir = Path(en_pa)
            if win_dir.exists():
                pat = True
                os.chdir(en_pa)
                path = en_pa
            else:
                en_pa = input(" Kindly Enter valid path")
                continue
    """
    def RmSpaceConvertFloat(x):
        return float(x.strip())


    def RmSpace(x):
        return x.strip()

    k1=[]
    k1 += [each for each in os.listdir(path) if each.endswith('.tuv')]
    '''
    for i, j, k11 in os.walk(path):
        # to get all filesname in k11
        print()

    for w in k11:
        #print(w)
        if w.split('.')[-1]=='tuv':
            k1.append(w)
            #to get only .tuv file in folder


    # helloContent[30]  // heading of data
    # helloContent[31]  // first data


    ch=helloContent[31].split('  ')
    velocity=RmSpaceConvertFloat(ch[-8])
    Long=ch[2]
    lat=ch[3]
    '''
    count = 0
    # csv parametrs Heading

    rows = []
    row = []

    for k in k1:
        # print(i[10:20:1])
        date = k[10:20:1].split(
            '_')[0] + "-" + k[10:20:1].split('_')[1] + "-" + k[10:20:1].split('_')[2]
        sitecode = k[5:9:1]
        helloFile = open(path + k)
        helloContent = helloFile.readlines()
        StopCount = helloContent.index('%TableEnd:\n')
        # 31st line from top is the useful data for us
        for a in range(31, StopCount - 1):
            res = helloContent[a].split('  ')
            ch = [ele for ele in res if ele.strip()]
            #print(ch)
            velocity = RmSpaceConvertFloat(ch[-4])
            CurrentDirection = RmSpaceConvertFloat(ch[-3])
            time = k[21:25:1]
            dateTime=date+" "+time[0:2:1]+":"+time[2:4:1]
            Long = ch[0]
            lat = ch[1]
            count += 1
            row = (str(count) +"," +date +"," +time +","+Long +"," +lat +","+dateTime+","+str(velocity)+","+str(CurrentDirection)+","+sitecode).split(',')  # create row for CSV
            # print(k)
            #print("Wait........")
            #print(row)  # block it
            rows.append(row)
            ch = ""
            velocity = ""
            Long = ""
            lat = ""
            time = ""
    fields = ['Sl.No',
        'Date',
        'Time',
        'long',
        'Lat','Date Time',
        'Velocity (cm/s)','Current Direction',
        'SiteCode']
    filename = "ZTime_Series"+"_"+now.strftime("%Y_%m_%d_%H%M%S")+".csv"

    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        # writing the data rows
        csvwriter.writerows(rows)
    print(" File is Saved as: "+ filename+" Saved in Path: "+ path)
    #rows = []
