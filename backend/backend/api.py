from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView

import pymongo
import json
import pymongo
import json
from bson import ObjectId 



client = pymongo.MongoClient("mongodb+srv://tashwani475:j56dRmajznRHWYV3@cluster0.4kmsi7u.mongodb.net/")
db = client['newDB1']
collection = db['sample']

cursor = collection.find()
data = list(cursor)
for item in data:
    item['_id'] = str(item['_id'])
json_string = json.dumps(data)

data = json.loads(json_string)
num_pairs = len(data[0]["pairs"])

print("Number of pairs:", num_pairs)
print(data[0]["schemaVersion"])
y=data[0]["pairs"][0]["baseToken"]["symbol"]
print(data[0]["pairs"][0]["baseToken"]["symbol"])






@api_view(['post'])
def get_data(request):
    pairAddress_ = request.data
    print(pairAddress_['body'])
    pairAddress_=pairAddress_['body']
    data = json.loads(json_string)
    num_pairs = len(data[0]["pairs"])
    price_native=''
    price_usd=''
    volume=[]
    for i in (0,num_pairs-1):
        if pairAddress_ == data[0]["pairs"][i]["pairAddress"]:
            price_native=data[0]["pairs"][i]["priceNative"]
            price_usd=data[0]["pairs"][i]["priceUsd"]
            volume=data[0]["pairs"][i]["volume"]
    print('price_usd',price_usd)
    print('price_usd',price_native)
    return JsonResponse({'price_usd':price_usd,'price_native':price_native,'volume':volume})