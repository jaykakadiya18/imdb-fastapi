import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = ""
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.data

