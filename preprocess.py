import pyspark
import requests
from pymongo import MongoClient




def get_station_information():
    url = "https://gbfs.citibikenyc.com/gbfs/en/station_information.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['data']['stations']
    else:
        print("Failed to retrieve station status data")
        return None

def write_to_mongo(stations):
    # MongoDB connection
    client = MongoClient("mongodb://localhost:27017/")
    db = client['project']
    collection = db['station_information']

    # Insert data into MongoDB
    if stations:
        collection.insert_many(stations)

station_info = get_station_information()
if station_info:
    write_to_mongo(station_info)