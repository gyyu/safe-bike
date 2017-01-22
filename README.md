# Safe Bike

Safe Bike is a web app geared towards promoting societal well-being by ensuring safer, more secure bike rides. Biking is a mode of transportation that is common to people of all socioeconomic and cultural backgrounds, and is simply a common-sense, clean, and easy way to get around the city (and get exercise)! Safe Bike is easy to use and understand, and aggregates millions of points of data in order to ensure your next trip is the best and safest one yet.

Made during PennApps XV, January 20-22, 2017.

### How to use Safe Bike

Simply install Flask and deploy. 
	
1. Clone or download a .zip and extract this repository
2. Install Flask
	
	pip3 install flask

3. Launch the web app
	
	python3 webpage.py

### Features of Safe Bike

- heatmaps of crime data and street lighting across Philadelphia that are easy to understand
- markers for bike racks and bike share locations
- outline of best bike routes
- geolocation
- routing and autofill for addresses using Google Maps
- ability to drag and drop route in order to best fit your needs
- generation of text directions along sidebar of page

### How we made Safe Bike

In order to make the web app:

- Flask (Python)
- HTML
- CSS
- JavaScript
- jQuery
- Google Maps API (for representing data points and routing between start and end destinations)

In order to parse and sort through millions of data plots:

- Python (scripts used to reduce data can be found in the data file)

Other sources:

- GitHub (for managing version control)
- OpenDataPhilly (for gathering data about crime incidents, street lighting, bike shares, and bike racks)
	- A part of the Open Government Initiative: [https://www.opendataphilly.org]
