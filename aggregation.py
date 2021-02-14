import pymongo
import config

conn = config.MONGO_URL
client = pymongo.MongoClient(conn)
db = client["movies_test"]
collection1 = db.movies_collection_test
collection2 = db.budget_collection_test
collection3 = db.aggregated_collection_test


data = list(collection1.aggregate([

    {"$lookup": {
        "from": "budget_collection_test",
        "localField": "original_title",
     "foreignField": "title",
     "as": "aggregate"
     }

     },
]))


collection3.insert_many(data)
print(f'{len(data)} is the number of movies inserted in the aggregated_collection')
