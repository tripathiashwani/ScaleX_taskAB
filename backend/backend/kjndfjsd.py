import pymongo
from pymongo import MongoClient
import simplejson as json

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://tashwani475:j56dRmajznRHWYV3@cluster0.4kmsi7u.mongodb.net/")
db = client['newDB1']
collection = db['sample']  # Change this to your collection name


data = json.loads(collection)
print (data['innerSet'][0]['rpasState'][0]['remoteRPAsDataLinkStatus'][0]['connectivityStatus'])

# CRUD Operations

# Create
# def create_crypto_data(data):
#     collection.insert_one(data)

# Read
# def read_all_crypto_data():
#     return list(collection.find())

# Update
# def update_crypto_data(query, new_data):
#     collection.update_one(query, {"$set": new_data})

# Delete
# def delete_crypto_data(query):
#     collection.delete_one(query)

# Test CRUD Operations

# @api_view(['get'])
# def get_prices(request):
#     all_=collection.find()
#     # print(updated.modified_count)
#     for x in all_:
#         print(x)
#     return JsonResponse({'data':'fsdfsdf'})

# if __name__ == "__main__":
#     # Test Create
#     sample_data = {
#         "pair": "DOJO/INJ", 
#         "price_usd": 0.004546,
#         "volume_h24": 270809.37
#     }
#     create_crypto_data(sample_data)

#     # Test Read
#     all_data = read_all_crypto_data()
#     print("All Crypto Data:")
#     for data in all_data:
#         print(data)

    # Test Update
    # update_query = {"pair": "DOJO/INJ"}
    # update_data = {"price_usd": 0.004600}
    # update_crypto_data(update_query, update_data)

    # updated_data = collection.find_one(update_query)
    # print("Updated Crypto Data:")
    # print(updated_data)

    # Test Delete
    # delete_query = {"pair": "DOJO/INJ"}
    # delete_crypto_data(delete_query)
    # print("Data deleted.")

    # Verify deletion
    # remaining_data = read_all_crypto_data()
    # print("Remaining Crypto Data:")
    # for data in remaining_data:
    #     print(data)


# import pymongo
# pair_address='inj17ufy5gqw33t0prwhkwa6ensv0jpj3xfvylgx8j'
# client = MongoClient("mongodb+srv://tashwani475:j56dRmajznRHWYV3@cluster0.4kmsi7u.mongodb.net/")
# db = client['newDB1']
# collection = db['sample']  # Change this to your collection name
# def get_price_native(pair_address):
#     # Connect to MongoDB
#     # Query MongoDB for the document with the given pair address
#     document = collection.find_one({"chainID": "injective"})
#     # db.test.find({“fruits.banana”:{$elemMatch: {“name”:“goodBanana”}}})
#     # first_pair = collection.find_one({})
#     pair_count = collection.count_documents({})
#     print("first pair",pair_count)
#     print("-------------------------------------------------------->>>>>>>>>>>>>>>")
#     all_=collection.find()
#     for x in all_:
#         print(x)
#     print("-------------------------------------------------------->>>>>>>>>>>>>>>")
#     print(document)
#     if document:
#         # Extract and return the priceNative
#         return document.get("priceNative")
#     else:
#         # Return None if the document is not found
#         return None

# # Example usage
# # pair_address = "inj17ufy5gqw33t0prwhkwa6ensv0jpj3xfvylgx8j"  # Example pair address
# # mongodb_uri = "mongodb://localhost:27017/"  # Example MongoDB URI
# # database_name = "your_database_name"  # Update with your database name
# # collection_name = "your_collection_name"  # Update with your collection name

# @api_view(['get'])
# def get_prices(request):
#     price_native = get_price_native(pair_address)
#     print("Price Native:", price_native)
#     return JsonResponse({'data':'fsdfsdf'})
