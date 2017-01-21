import csv

count = 0
f = open('latlong2.txt', 'w')
with open('Street_Poles.csv', newline='') as csvfile:
    #dialect = csv.Sniffer().sniff(csvfile.read(1024))
    #csvfile.seek(0)
    #reader = csv.reader(csvfile, dialect)
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if count!=0:
            f.write('new google.maps.LatLng('+row[1]+','+row[0]+'),')
        if count == 0:
            count +=1