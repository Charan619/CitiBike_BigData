from pymongo import MongoClient
from datetime import datetime 
import pandas as pd

def find_nearest_stations(latitude, longitude):
    # MongoDB connection
    client = MongoClient("mongodb://localhost:27017/")
    db = client['project']  
    station_information = db['station_information']

    query = {
        "location": {
            "$near": {
                "$geometry": {
                    "type": "Point",
                    "coordinates": [longitude, latitude]
                }
            }
        }
    }

    # Fetch the 10 nearest documents
    nearest_documents = station_information.find(query).limit(10)
    clean_data = clean_station_information(list(nearest_documents)) 
    return clean_data

def clean_station_information(docs):

    output_data = []
    for doc in docs:
        row = { "coords" : [doc['lat'], doc['lon']] , "StationName" : doc['name'], "StationID" : doc['station_id'], "ExtId":  doc['external_id'], "shortName": doc["short_name"] }
        output_data.append(row)
    
    return output_data

def find_station_status(stations, startorend):

    
    # MongoDB connection
    client = MongoClient("mongodb://localhost:27017/")
    db = client['project']  
    station_status = db['station_status'] 
    for station in stations: 
        if startorend == "B":
            parameter = "num_bikes_available"
        elif startorend == "E":
            parameter = "num_docks_available"

        station_data = station_status.find_one({"station_id": station["StationID"]}, {"_id": 0, parameter: 1})
        station[parameter]  = station_data
    return stations


def get_priority_score(stations, startorend):


    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(time, type(time))
    
    if startorend == "B":
        parameter = "num_bikes_available"
    elif startorend == "E":
        parameter = "num_docks_available"

    for station in stations: 
        if station[parameter] != 0: 
            priority = calculate_priority(station["shortName"], time)
            station["priority"] = priority
        else:
            stations.remove(station)

    if startorend == "B":
        sorted_data = sorted(stations, key=lambda item: item['priority'], reverse=False)
    elif startorend == "E":
        sorted_data = sorted(stations, key=lambda item: item['priority'], reverse=True)
    
    return sorted_data

def calculate_priority(station_id, datetime_str):

    file_path = 'aggregated_bike_data.csv'
    data = pd.read_csv(file_path)
    # Convert datetime string to dayofweek and time_category
    dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
    # Extract the day of the week (Monday=1, Sunday=7)
    dayofweek = dt.weekday() + 1
    hour = dt.hour
    if 0 <= hour <= 4:
        time_category = 'night'
    elif 5 <= hour <= 11:
        time_category = 'morning'
    elif 12 <= hour <= 16:
        time_category = 'afternoon'
    elif 17 <= hour <= 23:
        time_category = 'evening'
    else:
        return None  # Return None if the hour doesn't fit any category
    
    # Filter the data for the given station_id, dayofweek, and time_category
    result = data[(data['station_id'] == station_id) &
                  (data['dayofweek'] == dayofweek) &
                  (data['time_category'] == time_category)]
    
    # Check if there's a corresponding entry in the DataFrame
    if not result.empty:
        # Assuming bike_availability_diff is averaged or similarly aggregated, if multiple, return the first
        return result.iloc[0]['bike_availability_diff']
    else:
        return None  # Return None if no data is found
