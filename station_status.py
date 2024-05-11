import requests
import schedule
import time
from pymongo import MongoClient

def get_station_status():
    url = "https://gbfs.citibikenyc.com/gbfs/en/station_status.json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
        print(len(data['data']['stations']))
        return data['data']['stations']
    except requests.RequestException as e:
        print(f"Failed to retrieve station status data: {e}")
        return None

def write_to_mongo(stations):
    # MongoDB connection
    client = MongoClient("mongodb://localhost:27017/")
    db = client['project']
    collection = db['station_status']

    # Update data in MongoDB or insert if not exists
    if stations:
        for station in stations:
            query = {'station_id': station['station_id']}
            update = {'$set': station}
            collection.update_one(query, update, upsert=True)
        print("Data has been updated/inserted successfully.")

def job():
    print("Fetching station status...")
    stations = get_station_status()
    print("Ststaions")
    if stations:
        write_to_mongo(stations)

# Schedule the job every 10 minutes
schedule.every(1).minutes.do(job)

# Initial run to start immediately
job()

# Keep the 
# script running
while True:
    schedule.run_pending()
    time.sleep(1)