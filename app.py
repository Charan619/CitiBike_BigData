from flask import Flask, render_template, request
from pymongo import MongoClient
from data_processing import *
from geopy.geocoders import Nominatim
from datetime import datetime 

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client['project']  
station_status = db['station_status'] 
station_information = db['station_information']

@app.route('/submit', methods=['POST'])
def submit():
    start = request.form['starting_location']
    end = request.form['end_location']
    # Instantiate a new Nominatim client
    app = Nominatim(user_agent="tutorial")
    start_location = app.geocode(start).raw
    end_location = app.geocode(end).raw
    start_station =  get_priority_score(find_station_status(find_nearest_stations(float(start_location['lat']), float(start_location['lon'])), "B"), "B")
    stop_station =   get_priority_score(find_station_status(find_nearest_stations(float(end_location['lat']) , float(end_location['lon'])), "E"), "E")
    return render_template('map.html', start_location= [float(start_location['lat']), float(start_location['lon'])], 
                           end_location=[float(end_location['lat']) , float(end_location['lon'])], start_stations = start_station, stop_stations = stop_station)


@app.route('/')
def index():
    # Example coordinates: List of (latitude, longitude) tuples
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)