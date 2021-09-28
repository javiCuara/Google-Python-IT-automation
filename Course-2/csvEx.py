#! /bin/env python3

import csv 

def openCSV(file):
    f = open(file)
    csv_f =  csv.reader(f)

    for row in csv_f:
        name, phone, role = row
        print("Name: {}, Phone: {}, Role: {}".format(name,phone,role))

    f.close()

def writeCSV(data,file):
    with open(file, "w") as c:
        writer = csv.writer(c)
        writer.writerows(data)

rnd_data = [["workstation.local","192.168.25.46"],["webserver.cloud","10.2.5.6"]]

writeCSV(rnd_data,"rnd.csv")

