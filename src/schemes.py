from pydantic import BaseModel
from typing import List

class MovieRequest(BaseModel):
    movie_id: int

class MovieResponse(BaseModel):
    recommend_movies: List[int]

# class UserRequest(BaseModel):
#     user_id: int