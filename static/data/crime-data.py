import csv

def getLocation(point):
    space = point.index(' ', 6)
    return "(" + point[space+1:-1] + ", " + point[7:space] + ")"

def getCrimeWeight(crime):
    if crime == "Aggravated Assault No Firearm":
        return "1.5"
    elif "Firearm" in crime:
        return "2"
    elif "Homicide" in crime:
        return "2"
    elif crime == "Rape":
        return "2"
    elif "Sex Offenses" in crime:
        return "2"
    elif crime == "Arson":
        return "1.5"
    elif "Children" in crime:
        return "1.5"
    elif crime == "Burglary Non-Residential":
        return "1.5"
    elif crime == "Motor Vehicle Theft":
        return "1.5"
    elif "Narcotic" in crime:
        return "0.25" 
    elif "Fraud" in crime:
        return "0.25"
    elif "Disorderly Conduct" in crime:
        return "0.5"
    elif "Prostitution" in crime:
        return "0.25"
    elif "Forgery" in crime:
        return "0.25"
    elif "Embezzlement" in crime:
        return "0.25"
    elif "Liquor Law Violation" in crime:
        return "0.25"
    elif "Public Drunkenness" in crime:
        return "0.5"
    elif "Gambling" in crime:
        return "0.25"
    else:
        return "1"

count = 0
f = open('crime-data-latlong.txt', 'w')
with open('./PPD_Crime_Incidents_2006-Present.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if count != 0 and row[3][:4] == "2015":
            if row[10] != "" and row[9] != "":
                f.write("{location: new google.maps.LatLng" + 
                        getLocation(row[10]) + ", weight: " + 
                        getCrimeWeight(row[9]) + "},")
        if count == 0:
            count += 1

