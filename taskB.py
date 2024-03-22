import pymongo
from pymongo import MongoClient
import simplejson as json


import json

# Load JSON data
client = MongoClient("mongodb+srv://tashwani475:CcoOwcyNE8OJGdhE@cluster1.vxzjw6p.mongodb.net/")
db = client['newDB1']
collection = db['sample2']  # Change this to your collection name

from pymongo import MongoClient


# 1. Create (Insert)
new_entry = {
    "pair": {
        "name": "New Pair",
        "pairAddress": "new_pair_address",
        "baseToken": {"name": "Base Token", "symbol": "BASE"},
        "quoteToken": {"name": "Quote Token", "symbol": "QUOTE"},
        "price": {"usd": 10.0},
        "volume": {"24hours": 1000},
        "liquidity": {"usd": 500},
        "createdAt": 1710685033000
    }
}
insert_result = collection.insert_one(new_entry)
print("Inserted ID:", insert_result.inserted_id)

# 2. Read (Retrieve)
print("Data after insertion:")
for entry in collection.find():
    print(entry['pair'])

# 3. Update (Modify)
collection.update_one({'pair.name': 'New Pair'}, {'$set': {'pair.name': 'Updated Pair'}})

# 4. Delete (Remove)
delete_result = collection.delete_one({'pair.name': 'Updated Pair'})
print("Deleted Count:", delete_result.deleted_count)
