from http import client
from pymongo import MongoClient
from decouple import config
client = MongoClient(config("mongo_url"))
db = client['Employee']
collection = db['User']
collection2 = db['details']
collection3 = db['rabbitmq']

result = db['User'].aggregate([
    {
        '$lookup': {
            'from': 'details', 
            'localField': 'emp_id', 
            'foreignField': 'emp_id', 
            'as': 'details'
        }
    }
])


# -------------------------
# @user.get("/all/", tags=["emp_detailssssvbvbfsssss"])
# async def get_entity():
#     a = serializeList(collection.find())
#     b = serializeList(collection2.find())
#     c = a + b
#     return c