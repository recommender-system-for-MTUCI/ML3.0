import uvicorn
from fastapi import FastAPI, HTTPException

from src.schemes import MovieRequest, MovieResponse
from models.knn.app.recommend_function import get_recommendations


app = FastAPI()

@app.get('/home')
async def home():
    return "Ok"

@app.post('/predict', response_model=MovieResponse)
async def predict(request: MovieRequest):
    try:
        recommendations = get_recommendations(request.movie_id)
        return {'recommend_movies': recommendations}
    except:
        raise HTTPException(status_code=404, detail="Film ID not found.")
    

# if __name__ == 'main':
#     uvicorn.run('main:app', reload=True)