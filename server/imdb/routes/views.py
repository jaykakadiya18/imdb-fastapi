from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
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
            `/movie` For All of the movies\n
            

            Get dict: List of movies
    """
    # print(type(data))
    movie = await findone_document(name)
    return {"Movies": str(movie)}



@router.post("/", dependencies=[Depends(Auth_handler)])
async def add_movies(data: MoviesSchema):
    """
    Add movie in database
    """
    movie = await create_document(data) #Data add in movies database
    return {"Data Added": movie}

@router.put("/{id}", dependencies=[Depends(Auth_handler)])
async def update_movies(id: str, data: MoviesSchema):
    """
    Update movie in database
    """
    # Check if ObjectID is valid
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail=f"Invalid ID - {id}")

    #Data update in movies database
    data = await update_document(id, data)
    if not data:
        raise HTTPException(status_code=404, detail=f"Your id {id} does not exist!!!")
    return {"Data Updated": data}


@router.delete("/{id}", dependencies=[Depends(Auth_handler)])
async def delete_movies(id: str):
    """
    Delete movie in database
    """
    # Check if ObjectID is valid
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail=f"ID - {id} is Invalid")
    
    #Data delete in movies database
    data = await delete_document(id)
    if not data:
        raise HTTPException(status_code=500, detail=f"ID is - {id} Failed to Delete")
    return {"Data Deleted": data}
   

