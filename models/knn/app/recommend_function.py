import joblib
import pandas as pd

df = pd.read_csv('data/dataset_23k_v2.csv')
cos_sim = joblib.load('models/knn/weights/cosine_similarity.pkl')

def get_recommendations(id: int, cosine_sim=cos_sim, popularity_threshold=0.65):

    idx = df[df['id'] == id].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:]  # Убираем сам фильм
    movie_indices = [i[0] for i in sim_scores]

    popular_movies = df.iloc[movie_indices][:10]
    popular_movies = popular_movies[popular_movies['weight_rating'] >= popularity_threshold][:10]

    return popular_movies['id'].tolist()
