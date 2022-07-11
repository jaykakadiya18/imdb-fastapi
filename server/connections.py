import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb+srv://jaykakadiya:jaykakadiya@cluster0.ddma8.mongodb.net/test"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.data

