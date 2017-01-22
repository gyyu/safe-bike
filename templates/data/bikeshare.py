import json
import yaml

def formatCoordinates(point):
    space = point.index(' ')
    return "(" + point[space+1:-1] + ", " + point[1:space-1] + ")"

f=open('bike-share.txt', 'w')
j=open('bikeshare.json')
data = yaml.safe_load(j)
for i in data["features"]:
	f.write("{ position: new google.maps.LatLng" +
    		formatCoordinates(str(i["geometry"]["coordinates"])) + ", type: 'share'},")