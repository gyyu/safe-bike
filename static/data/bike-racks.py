import csv

def getLocation(point):
    space = point.index(' ')
    return "(" + point[space+1:-1] + ", " + point[1:space-1] + ")"

count = 0
f = open('bike-rack.txt', 'w')
with open('Bike_Racks.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if count != 0 and int(row[1]) > 2:
            f.write("{ position: new google.maps.LatLng" + 
	                getLocation(row[2]) + ", type: 'biking'},")
        if count == 0:
            count += 1
