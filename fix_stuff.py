from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['project']
collection = db['station_information']

# collection.update_many(
#     {},
#     [{
#         "$set": {
#             "location": {
#                 "type": "Point",
#                 "coordinates": ["$lon", "$lat"]
#             }
#         }
#     }],
#     array_filters=[]
# )

collection.create_index([("location", "2dsphere")])