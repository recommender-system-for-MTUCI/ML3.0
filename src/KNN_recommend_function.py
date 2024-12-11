import joblib
import pandas as pd
from config.settings import settings

df = pd.read_csv(settings.DATASET_PATH)
cos_sim = joblib.load(settings.MODEL_PATH)

def get_recommendations(id: int, cosine_sim=cos_sim, popularity_threshold=settings.POPULARITY_THRESHOLD, 
                        max_recommendations=settings.MAX_RECOMMENDATIONS, data=df):

    idx = data[data['id'] == id].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:]  # Убираем сам фильм
    movie_indices = [i[0] for i in sim_scores]

    popular_movies = data.iloc[movie_indices]
    popular_movies = popular_movies[popular_movies['weight_rating'] >= popularity_threshold][:max_recommendations]

    return popular_movies['id'].tolist()
