import uvicorn
from fastapi import FastAPI, HTTPException
from config.settings import settings

from src.schemes import MovieRequest, MovieResponse
from src.KNN_recommend_function import get_recommendations


__version__ = settings.VERSION

app = FastAPI()


@app.get('/version')
async def home():
    return {'version': __version__}

@app.get('/predict/{movie_id}')
async def predict(movie_id:int):
    try:
        movie_id = int(movie_id)
        recommendations = get_recommendations(movie_id)
        return {'recommend_movies': recommendations}
    except IndexError:  
        raise HTTPException(status_code=404, detail="Film ID not found.")
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))

'''
if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000)
'''