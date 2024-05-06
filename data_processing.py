from pymongo import MongoClient


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
        row = { "coords" : [doc['lat'], doc['lon']] , "StationName" : doc['name'], "StationID" : doc['station_id'], "ExtId":  doc['external_id'] }
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