from server.connections import database
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId

# Get collection from database instance
collection = database.get_collection("movies")

# Add New Movie
async def create_document(doc_data: dict) -> dict:

    """Create a single IMDB Movie document in movies collection.

    Returns:
        Dict: New Movie detail
    """

    doc = jsonable_encoder(doc_data)
    doc = await collection.insert_one(doc)
    new_doc = await collection.find_one({"_id": doc.inserted_id}, projection={'_id': False})
    return new_doc

async def findone_document(name: str) -> dict:
    try:
        mydocument = []
        # async for document in collection.find({'name': { "$regex": "^" + name}}):
        
        async for document in collection.find({'name': { "$regex": name.capitalize()}}):
            mydocument.append(document)
        return mydocument
    except:
        mydocument = []
        async for document in collection.find():
            mydocument.append(document)

        return mydocument

    # loop = client.get_io_loop()
    # loop.run_until_complete(do_find())


async def fetch_documents_all(movie: list) -> list:

    """Fetch all documents from movies collection 

    Returns:
        List: List of movies
    """

    data = []
    async for doc in collection.find(movie):
        data.append(doc)
    return data


async def update_document(_id:str, doc_data: dict) -> dict:

    """update a single IMDB Movie document in movies collection.

    Returns:
        Dict: updated Movie detail
    """

    doc = jsonable_encoder(doc_data)
    doc = await collection.replace_one({'_id': ObjectId(_id)}, doc)
    if doc.modified_count == 0:
        return False
    new_doc = await collection.find_one({"_id": ObjectId(_id)}, projection={'_id': False})
    return new_doc


async def delete_document(_id:str) -> bool:
    
    """Delete a single IMDB Movie document in movies collection.

    Args:
        _id (str): Object ID belonging to a particular doc

    Returns:
        bool: Delete reponse
    """

    doc = await collection.delete_one({'_id': ObjectId(_id)})
    return True
