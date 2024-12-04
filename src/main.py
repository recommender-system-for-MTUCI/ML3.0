import uvicorn
from fastapi import FastAPI, HTTPException

from src.schemes import MovieRequest, MovieResponse
from models.knn.app.recommend_function import get_recommendations

__version__ = '0.0.1'
app = FastAPI()

@app.get('/version')
async def home():
    return {'version': __version__}

@app.post('/similar_films', response_model=MovieResponse)
async def predict(request: MovieRequest):
    try:
        recommendations = get_recommendations(request.movie_id)
        return {'recommend_movies': recommendations}
    except:
        raise HTTPException(status_code=404, detail="Film ID not found.")
    

# if __name__ == 'main':
#     uvicorn.run('main:app', reload=True)