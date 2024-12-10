from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    # Параметры приложения
    APP_NAME: str = "Movie Recommendation API"
    VERSION: str = "0.0.1"

    # Пути к данным
    DATASET_PATH: Path = Path("data/dataset_23k_v2.csv")
    MODEL_PATH: Path = Path("models/knn/weights/cosine_similarity.pkl")

    # Параметры рекомендаций
    POPULARITY_THRESHOLD: float = 0.65
    MAX_RECOMMENDATIONS: int = 10


# Инициализация настроек
settings = Settings()
