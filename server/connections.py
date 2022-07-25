import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "" #add mongodb server 
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.data

