from server.connections import database
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId
import uuid
from server.admin.models.schema import (
     UserInDB
)
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

# Get collection from database instance
collection = database.get_collection("accounts")

# Database operations

async def fetch_user(parameters: dict, hashed_password=False) -> dict:

    """Fetch single document from accounts collection based on user parameters passed

    Returns:
        Dict: User account detail
    """

    project = {'_id': False} if hashed_password else {'_id': False, 'hashed_password': False}
    user = await collection.find_one(parameters, projection=project)
    return user

# async def fetch_users_all() -> list:

#     """Fetch all documents from accounts collection 

#     Returns:
#         List: List of user details
#     """

#     data = []
#     async for doc in collection.find({}, projection={'_id': False, 'hashed_password': False}):
#         data.append(doc)
#     return data

async def create_user(doc_data: dict) -> dict:

    """Create a single user document in accounts collection upon new user registration

    Returns:
        Dict: User account detail
    """

    hashed_password = get_password_hash(doc_data.password)
    user_in_db = jsonable_encoder((UserInDB(
        **doc_data.dict(), hashed_password=hashed_password, user_id=str(uuid.uuid1()), role='admin'
        )))
    doc = await collection.insert_one(user_in_db)
    new_doc = await collection.find_one({"_id": doc.inserted_id}, projection={'_id': False, 'hashed_password': False})
    return new_doc