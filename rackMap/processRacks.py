import csv

count = 0
f = open('rack-data-latlong.txt', 'w')
with open('./Bike_Racks.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if row[2] != "":
            f.write("new google.maps.LatLng" + row[2]+ ",")
        if count == 0:
            count += 1