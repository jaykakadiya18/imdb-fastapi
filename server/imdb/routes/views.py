from typing import Optional, List
from fastapi import APIRouter, Body, Request, Depends, HTTPException
from bson.objectid import ObjectId
from server.imdb.models.schema import (
    MoviesSchema
)
from server.imdb.models.database import (
    create_document, update_document, delete_document,findone_document
)

from server.admin.routes.views import JWTBearer

EXCEPTION_RESPONSE = "Something went wrong! Report issue"

router = APIRouter()

Auth_handler = JWTBearer(["admin"])

@router.get("/search", response_description="")
async def search_movies(name: Optional[str] = None):
    """
        You you don't know full name of movie then       

            Examples of search you can :
            `/movie?search=The Wizard of Oz`\n
            `/movie?search=Wizard`\n
            `/movie?search=Wizard of Oz`\n
            `/movie?search=the wizard of oz`\n
            `/movie?sortby=oz`\n
            `/movie?search=the`\n
            `/movie`\n
            Returns:
                dict: List of movies
    """
    # print(type(data))
    movie = await findone_document(name)
    return {"Data Found": str(movie)}



@router.post("/", dependencies=[Depends(Auth_handler)])
async def add_movies(data: MoviesSchema):
    # Create document in MongoDB
    movie = await create_document(data)
    return {"Data Added": movie}

@router.put("/{movie_id}", dependencies=[Depends(Auth_handler)])
async def update_movies(movie_id: str, data: MoviesSchema):

    # Check if ObjectID is valid
    if not ObjectId.is_valid(movie_id):
        raise HTTPException(status_code=400, detail=f"Invalid ID - {movie_id}")

    # Update document in MongoDB with help of MovieId/ObjectId
    data = await update_document(movie_id, data)
    if not data:
        raise HTTPException(status_code=404, detail=f"Your id {movie_id} does not exist!!!")
    return {"Data Updated": data}


@router.delete("/{movie_id}", dependencies=[Depends(Auth_handler)])
async def delete_movies(movie_id: str):

    # Check if ObjectID is valid
    if not ObjectId.is_valid(movie_id):
        raise HTTPException(status_code=400, detail=f"Invalid ID - {movie_id}")
    
    # Delete document in MongoDB with help of MovieId/ObjectId
    data = await delete_document(movie_id)
    if not data:
        raise HTTPException(status_code=500, detail=f"Failed to Delete - {movie_id}")
    return {"Data Deleted": data}
   

