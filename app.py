from flask import Flask, render_template, request
from pymongo import MongoClient
from data_processing import *
from geopy.geocoders import Nominatim

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client['project']  
station_status = db['station_status'] 
station_information = db['station_information']

@app.route('/submit', methods=['POST'])
def submit():
    address = request.form['location']
    geolocator = Nominatim(user_agent="bigDataProject")
    location = geolocator.geocode(address)
    if location:
        coordinates = (location.latitude, location.longitude)
        print(coordinates)
        return True
    else:
        return False
    #     return f"Coordinates for '{address}': {coordinates}"
    # else:
    #     return "Location not found. Please enter a valid address."


@app.route('/')
def index():

    start_lat = 40.703661705241345 
    start_lon = -74.0131813287735

    stop_lat = 40.71907891179564
    stop_lon = -73.94223690032959

    start_station = find_station_status(find_nearest_stations(start_lat, start_lon), "B")
    stop_station = find_station_status(find_nearest_stations(stop_lat, stop_lon), "E")

    # Example coordinates: List of (latitude, longitude) tuples
    return render_template('index.html', start_stations = start_station, stop_stations = stop_station)

if __name__ == '__main__':
    app.run(debug=True)