from typing import List
from pydantic import BaseModel, Field


class MoviesSchema(BaseModel):
    popularity: float = Field(Ellipsis)
    director: str = Field(Ellipsis)
    genre: List[str] = Field(Ellipsis)
    imdb_score: float = Field(Ellipsis)
    name: str = Field(Ellipsis)

    class Config:
        schema_extra = {
            "example": {
                "popularity":11,
                "director": "mahesh babu",
                "genre": ["thriller", "action"],
                "imdb_score": 1.6,
                "name": "bahubali"
            }
        }


