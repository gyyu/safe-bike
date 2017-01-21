import csv

count = 0
f = open('latlong2.txt', 'w')
with open('crime_data.csv', newline='') as csvfile:
    #dialect = csv.Sniffer().sniff(csvfile.read(1024))
    #csvfile.seek(0)
    #reader = csv.reader(csvfile, dialect)
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if count!=0:
            point  = row[2]
            print(point)
            f.write('new google.maps.LatLng('+point[18:24]+','+point[7:14]+'),')
        if count == 0:
            count +=1